from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.views import auth_login
from django.contrib.auth import authenticate

from sample_admin_app.models import *

class PersonsView(TemplateView):
    template_name = "persons.html"

    def get(self, request, *args, **kwargs):
        context = super(PersonsView, self).get_context_data(**kwargs)
        members = Member.objects.all().select_related('person')
        context['members'] = members
        return render(self.request, self.template_name, context)

class CustomLoginView(TemplateView):
    template_name = "login.html"

    def get(self, _, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return auth_login(self.request, *args, **kwargs)

    def post(self, _, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)  # 1
        if user is not None:
            auth_login(self.request, user)
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return auth_login(self.request, *args, **kwargs)

    def get_next_redirect_url(self):
        redirect_url = self.request.GET.get('next')
        if not redirect_url or redirect_url == '/':
            redirect_url = '/persons/'
        return redirect_url