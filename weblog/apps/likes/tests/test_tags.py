from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from ..models import Like
from ..templatetags.pinax_likes_tags import (
    ObjectDecorator,
    who_likes as who_likes_tag,
    likes as likes_tag,
    likes_count as likes_count_tag
)


class ObjectDecoratorTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="patrick")
        self.other_users = []
        for other_user in ["james", "brian", "michael", "tom", "yulka"]:
            self.other_users.append(
                User.objects.create(username=other_user)
            )
        Like.objects.create(
            sender=self.user,
            receiver_content_type=ContentType.objects.get(model="user"),
            receiver_object_id=self.other_users[0].pk
        )

    def test_object_decorator(self):
        for obj in ObjectDecorator(self.user, self.other_users).objects():
            if obj.username == "james":
                self.assertTrue(obj.liked)
            else:
                self.assertFalse(obj.liked)

    def test_who_likes(self):
        likes = who_likes_tag(self.other_users[0])
        self.assertTrue(likes.filter(sender=self.user).exists())

    def test_likes_specific(self):
        likes = likes_tag(self.user, "auth.User")
        self.assertEquals(likes.count(), 1)
        self.assertEquals(likes[0].receiver, self.other_users[0])

    def test_likes_all(self):
        likes = likes_tag(self.user)
        self.assertEquals(likes.count(), 1)
        self.assertEquals(likes[0].receiver, self.other_users[0])

    def test_likes_count(self):
        self.assertEquals(likes_count_tag(self.other_users[0]), 1)
