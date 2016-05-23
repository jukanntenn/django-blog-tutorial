from django.contrib import auth
from django.views.generic.edit import FormView
from usera.forms import SignInForm, SignUpForm


class SignInView(FormView):
    template_name = ''
    form_class = SignInForm
    success_url = '/blog'

    def form_valid(self, form):
        user = form.get_user()
        auth.login(self.request, user)
        return super(SignInView, self).form_valid(form)


class SignUpView(FormView):
    template_name = ''
    form_class = SignUpForm
    success_url = '/blog'

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)
