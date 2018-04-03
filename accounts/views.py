from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, UpdateView,
                                  DetailView,)

from . import forms, models

# Create your views here.
class RegisterView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/register.html"

class ProfileEditView(UpdateView):
    fields = ('facebook','facebook_link',)
    template_name = 'registration/profile_edit.html'
    model = models.Profile

class ProfileDetailView(DetailView):
    context_object_name = 'profile'
    template_name = 'registration/profile_detail.html'
    model = models.Profile
