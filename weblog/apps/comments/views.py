from django.contrib.auth.decorators import login_required

from django_comments.views.comments import post_comment

post_comment = login_required(post_comment)

# Create your views here.

# class CommentPostView(LoginRequiredMixin, FormView):
#     form_class = comments.get_form()
#     preview = None
#     data = None
#     using = None
#
#     @csrf_protect
#     @require_POST
#     def dispatch(self, request, *args, **kwargs):
#         super(CommentPostView, self).dispatch(request, *args, **kwargs)
#
#     def get_form_kwargs(self):
#         kwargs = super(CommentPostView, self).get_form_kwargs()
#         kwargs['data'] = self.get_data()
#         kwargs['target'] = self.look_up_object()
#         return kwargs
#
#     def look_up_object(self):
#         data = self.get_data()
#         ctype = data.get("content_type")
#         object_pk = data.get("object_pk")
#         if ctype is None or object_pk is None:
#             return CommentPostBadRequest("Missing content_type or object_pk field.")
#         try:
#             model = apps.get_model(*ctype.split(".", 1))
#             target = model._default_manager.using(self.using).get(pk=object_pk)
#             return target
#         except TypeError:
#             return CommentPostBadRequest(
#                     "Invalid content_type value: %r" % escape(ctype))
#         except AttributeError:
#             return CommentPostBadRequest(
#                     "The given content-type %r does not resolve to a valid model." % escape(ctype))
#         except ObjectDoesNotExist:
#             return CommentPostBadRequest(
#                     "No object matching content-type %r and object PK %r exists." % (
#                         escape(ctype), escape(object_pk)))
#         except (ValueError, ValidationError) as e:
#             return CommentPostBadRequest(
#                     "Attempting go get content-type %r and object PK %r exists raised %s" % (
#                         escape(ctype), escape(object_pk), e.__class__.__name__))
#
#     def get_data(self):
#         if self.data is None:
#             self.data = self.request.POST.copy()
#
#             if self.request.user.is_authenticated():
#                 if not self.data.get('name', ''):
#                     self.data["name"] = self.request.user.get_full_name() or self.request.user.get_username()
#                 if not self.data.get('email', ''):
#                     self.data["email"] = self.request.user.email
#
#         return self.data
#
#     def get_preview(self):
#         if self.preview is None:
#             self.preview = 'preview' in self.get_data()
#         return self.preview
#
#     def get_using(self):
#         return self.using
#
#     def form_invalid(self, form):
#         if form.security_errors():
#             return CommentPostBadRequest(
#                 "The comment form failed security verification: %s" % escape(str(form.security_errors())))
#
#     def render_to_preview(self):
#         pass
