from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from apps.users.forms import CustomUserCreateForm


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreateForm

    def get_success_url(self):
        return reverse('login')

def landing_page(request):
    return render(request, 'landing.html')
