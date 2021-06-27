from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from beneficiario.models import Usuario
from django.views import generic
# Create your views here.


class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True, help_text='')

    class Meta:
        model = Usuario
        fields = ('username', 'nombre','password1','password2', )

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'