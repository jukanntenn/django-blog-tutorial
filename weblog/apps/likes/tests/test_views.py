import json
import mock

from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.http import Http404
from django.test import RequestFactory, TestCase
from django.utils.http import urlquote

from ..models import Like
from ..views import LikeToggleView


class LikeToggleTestCase(TestCase):

    def setUp(self):
        self.user_content_type = ContentType.objects.get(model="user")
        self.factory = RequestFactory()
        self.user = User.objects.create(username="patrick")
        self.other_users = []
        for other_user in ["james", "brian", "michael", "tom", "yulka"]:
            self.other_users.append(
                User.objects.create(username=other_user)
            )

        # Create a LIKE from Patrick for James.
        james = User.objects.get(username="james")
        self.original_like = Like.objects.create(
            sender=self.user,
            receiver_content_type=self.user_content_type,
            receiver_object_id=james.pk
        )
        self.like_qs = Like.objects.filter(
            sender=self.user,
            receiver_content_type=self.user_content_type

        )

        self.login_redirect = settings.LOGIN_URL

    def assertRedirectsToLogin(self, response, next):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            "{}?next={}".format(self.login_redirect, next)
        )

    def test_like_brian(self):
        """
        Ensure logged-in user can like another user.
        """
        brian = User.objects.get(username="brian")
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=self.user_content_type.pk,
                object_id=brian.pk
            )
        )
        request = self.factory.post(url)
        request.user = self.user

        self.assertFalse(self.like_qs.filter(receiver_object_id=brian.pk).exists())

        with mock.patch('pinax.likes.signals.object_liked.send', autospec=True) as mocked_handler:
            response = LikeToggleView.as_view()(
                request,
                content_type_id=self.user_content_type.pk,
                object_id=brian.pk
            )
            self.assertEqual(response.status_code, 302)
            self.assertTrue(self.like_qs.filter(receiver_object_id=brian.pk).exists())
            # Ensure signal handler was called with proper arguments.
            like = self.like_qs.get(receiver_object_id=brian.pk)
            self.assertEquals(mocked_handler.call_count, 1)
            mocked_handler.assert_called_with(sender=Like, like=like, request=request)

    def test_unauthed_like_brian(self):
        """
        Ensure anonymous user cannot like another user.
        """
        brian = User.objects.get(username="brian")
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=self.user_content_type.pk,
                object_id=brian.pk
            )
        )
        request = self.factory.post(url)
        request.user = AnonymousUser()
        response = LikeToggleView.as_view()(
            request,
            content_type_id=self.user_content_type.pk,
            object_id=brian.pk
        )
        self.assertRedirectsToLogin(response, urlquote(url))
        self.assertFalse(self.like_qs.filter(receiver_object_id=brian.pk).exists())

    def test_unlike_james(self):
        """
        Ensure a liked object is unliked.
        """
        james = User.objects.get(username="james")
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=self.user_content_type.pk,
                object_id=james.pk
            )
        )
        request = self.factory.post(url)
        request.user = self.user

        self.assertTrue(self.like_qs.filter(receiver_object_id=james.pk).exists())
        with mock.patch('pinax.likes.signals.object_unliked.send', autospec=True) as mocked_handler:
            response = LikeToggleView.as_view()(
                request,
                content_type_id=self.user_content_type.pk,
                object_id=james.pk
            )
            self.assertEqual(response.status_code, 302)
            self.assertFalse(self.like_qs.filter(receiver_object_id=james.pk).exists())
            # Ensure signal handler was called with proper arguments.
            self.assertEquals(mocked_handler.call_count, 1)
            mocked_handler.assert_called_with(sender=Like, object=james, request=request)

    def test_like_michael_ajax(self):
        """
        Ensure proper AJAX response for a like.
        """
        michael = User.objects.get(username="michael")
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=self.user_content_type.pk,
                object_id=michael.pk
            )
        )
        request = self.factory.post(url, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        request.user = self.user
        with mock.patch('pinax.likes.signals.object_liked.send', autospec=True) as mocked_handler:
            response = LikeToggleView.as_view()(
                request,
                content_type_id=self.user_content_type.pk,
                object_id=michael.pk
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(self.like_qs.filter(receiver_object_id=michael.pk).exists())
            data = json.loads(response.content.decode())
            self.assertEqual(data["likes_count"], 1)
            self.assertEqual(data["liked"], True)
            self.assertTrue("html" in data)
            # Ensure signal handler was called with proper arguments.
            like = self.like_qs.get(receiver_object_id=michael.pk)
            self.assertEquals(mocked_handler.call_count, 1)
            mocked_handler.assert_called_with(sender=Like, like=like, request=request)

    def test_multiple_like_michael_ajax(self):
        """
        Ensure multiple users can like the same object.
        """
        michael = User.objects.get(username="michael")
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=self.user_content_type.pk,
                object_id=michael.pk
            )
        )
        request = self.factory.post(url, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        request.user = self.user
        response = LikeToggleView.as_view()(
            request,
            content_type_id=self.user_content_type.pk,
            object_id=michael.pk
        )
        # Add a second LIKE
        request.user = User.objects.get(username="tom")
        response = LikeToggleView.as_view()(
            request,
            content_type_id=self.user_content_type.pk,
            object_id=michael.pk
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.like_qs.filter(receiver_object_id=michael.pk).exists())
        data = json.loads(response.content.decode())
        self.assertEqual(data["likes_count"], 2)
        self.assertEqual(data["liked"], True)
        self.assertTrue("html" in data)

    def test_unlike_james_ajax(self):
        """
        Ensure a liked object is unliked via AJAX.
        """
        james = User.objects.get(username="james")
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=self.user_content_type.pk,
                object_id=james.pk
            )
        )
        request = self.factory.post(url, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        request.user = self.user
        with mock.patch('pinax.likes.signals.object_unliked.send', autospec=True) as mocked_handler:
            response = LikeToggleView.as_view()(
                request,
                content_type_id=self.user_content_type.pk,
                object_id=james.pk
            )
            self.assertEqual(response.status_code, 200)
            self.assertFalse(self.like_qs.filter(receiver_object_id=james.pk).exists())
            data = json.loads(response.content.decode())
            self.assertEqual(data["likes_count"], 0)
            self.assertEqual(data["liked"], False)
            self.assertTrue("html" in data)
            # Ensure signal handler was called with proper arguments.
            self.assertEquals(mocked_handler.call_count, 1)
            mocked_handler.assert_called_with(sender=Like, object=james, request=request)

    def test_like_unlikeable_object(self):
        """
        Ensure proper error response when liking an unlikeable model.
        """
        # Test settings do not permit liking a models.Like instance.
        like_content_type = ContentType.objects.get(model="like")
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=like_content_type.pk,
                object_id=self.original_like.pk
            )
        )
        request = self.factory.post(url)
        request.user = self.user
        response = LikeToggleView.as_view()(
            request,
            content_type_id=like_content_type.pk,
            object_id=self.original_like.pk
        )
        self.assertEqual(response.status_code, 403)

    def test_like_bad_content_type(self):
        """
        Ensure we raise 404 when liking a bad ContentType.
        """
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=12345,
                object_id=1
            )
        )
        request = self.factory.post(url)
        request.user = self.user
        with self.assertRaises(Http404):
            LikeToggleView.as_view()(request, content_type_id=12345, object_id=1)

    def test_like_bad_object_id(self):
        url = reverse(
            "pinax_likes:like_toggle",
            kwargs=dict(
                content_type_id=self.user_content_type.pk,
                object_id=555
            )
        )
        request = self.factory.post(url)
        request.user = self.user
        with self.assertRaises(Http404):
            LikeToggleView.as_view()(
                request,
                content_type_id=self.user_content_type.pk,
                object_id=555
            )
