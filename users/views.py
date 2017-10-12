from django.urls import reverse
from django.views.generic import TemplateView
from allauth.account.views import LoginView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_success_url(self):
        return reverse('home')