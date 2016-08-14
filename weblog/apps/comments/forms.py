from django import forms
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_text
from django.utils import timezone

from django_comments.forms import CommentForm

from .models import CommentWithParent


class CommentWithParentForm(CommentForm):
    parent = forms.IntegerField(required=False, widget=forms.HiddenInput)

    def __init__(self, target_object, parent=None, data=None, initial=None, auto_id=False):
        self.parent = parent

        if initial is None:
            initial = {}
        initial.update({'parent': self.parent})
        super(CommentWithParentForm, self).__init__(target_object, data=data, initial=initial, auto_id=auto_id)
        del self.fields['name']
        del self.fields['email']
        del self.fields['url']

    def get_comment_model(self):
        return CommentWithParent

    def get_comment_create_data(self):
        """
        Returns the dict of data to be used to create a comment. Subclasses in
        custom comment apps that override get_comment_model can override this
        method to add extra fields onto a custom comment model.
        """
        return dict(
                content_type=ContentType.objects.get_for_model(self.target_object),
                object_pk=force_text(self.target_object._get_pk_val()),
                parent_id=self.cleaned_data['parent'],
                comment=self.cleaned_data["comment"],
                submit_date=timezone.now(),
                site_id=settings.SITE_ID,
                is_public=True,
                is_removed=False,
        )
