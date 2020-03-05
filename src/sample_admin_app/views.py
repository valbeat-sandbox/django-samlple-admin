from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from sample_admin_app.models import *

class PersonsView(TemplateView):
    template_name = "persons.html"

    def get(self, request, *args, **kwargs):
        context = super(PersonsView, self).get_context_data(**kwargs)
        members = Member.objects.all().select_related('person')
        context['members'] = members
        return render(self.request, self.template_name, context)