from django.contrib.auth.backends import ModelBackend

from .utils import _allowed, per_model_perm_check


class CanLikeBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = True

    def is_allowed(self, obj):
        return _allowed(obj)

    def has_perm(self, user, perm, obj=None):
        if perm == "likes.can_like":
            if not user.is_authenticated():
                return False
            return (self.is_allowed(obj) and per_model_perm_check(user, obj))
        return super(CanLikeBackend, self).has_perm(user, perm, obj)
