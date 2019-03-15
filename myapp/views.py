from django.views import generic

class HomeView(generic.TemplateView):
    template_name = 'home.html'

class SignIn(generic.TemplateView):
    template_name = 'signin.html'

class SignUp(generic.TemplateView):
    template_name = 'signup.html'

class TestTemplate(generic.TemplateView):
    template_name = "account/signup.html"