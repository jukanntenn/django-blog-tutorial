from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from usera.forms import SignInForm, SignUpForm


class SignInView(FormView):
    template_name = ''
    form_class = SignInForm
    success_url = '/blog'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
            else:
                pass
        else:
            pass
        return super(SignInView, self).form_valid(form)


class SignUpView(FormView):
    template_name = ''
    form_class = SignUpForm
    success_url = '/blog'

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)
