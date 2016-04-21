# -*- coding: utf-8 -*-
# Created on 21 Apr 2016 at 11:25
from __future__ import unicode_literals, absolute_import
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Missed
from .forms import MissedBinForm


class MissedListView(ListView):
    model = Missed

    def get_queryset(self):
        return Missed.objects.filter(reported_by=self.request.user)


class MissedCreateView(CreateView):
    model = Missed
    form_class = MissedBinForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.reported_by = self.request.user

        return super(MissedCreateView, self).form_valid(form)
