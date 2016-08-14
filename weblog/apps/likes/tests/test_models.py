from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from ..models import Like


class LikeTestCase(TestCase):

    def setUp(self):
        self.content_type = ContentType.objects.get(model="user")

    def test_unicode(self):
        u1 = User.objects.create(username="patrick")
        u2 = User.objects.create(username="james")
        like = Like(
            sender=u1,
            receiver_content_type=self.content_type,
            receiver_object_id=u2.pk
        )
        self.assertEquals(str(like), "patrick likes james")

    def test_like(self):
        u1 = User.objects.create(username="patrick")
        u2 = User.objects.create(username="james")
        like, liked = Like.like(u1, self.content_type, u2.pk)
        self.assertTrue(liked)
        self.assertEquals(str(like), "patrick likes james")

    def test_unlike(self):
        u1 = User.objects.create(username="patrick")
        u2 = User.objects.create(username="james")
        like, liked = Like.like(u1, self.content_type, u2.pk)
        like, liked = Like.like(u1, self.content_type, u2.pk)
        self.assertFalse(liked)
