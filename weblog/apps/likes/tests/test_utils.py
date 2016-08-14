from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from .models import Demo

from ..utils import _allowed, get_config, per_model_perm_check


class UtilsTestCase(TestCase):

    def setUp(self):
        self.content_type = ContentType.objects.get(model="user")

    def test_allowed_model(self):
        self.assertTrue(_allowed(User))

    def test_allowed_str(self):
        self.assertTrue(_allowed("auth.User"))

    def test_allowed_other(self):
        self.assertFalse(_allowed(TestCase))

    def test_get_config(self):
        config = get_config(User)
        self.assertEquals(config["css_class_on"], "fa-heart")

    def test_per_model_perm_check(self):
        patrick = User.objects.create_user(username="patrick")
        check = per_model_perm_check(patrick, User)
        self.assertTrue(check)

    def test_per_model_perm_check_default(self):
        patrick = User.objects.create_user(username="patrick")
        check = per_model_perm_check(patrick, Demo)
        self.assertTrue(check)
