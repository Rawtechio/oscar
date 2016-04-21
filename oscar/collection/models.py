# -*- coding: utf-8 -*-
# Created on 21 Apr 2016 at 11:20
from __future__ import unicode_literals, absolute_import


# Django
from django.db import models
from django.conf import settings

# 3rd Party
from model_utils.models import TimeStampedModel


class Missed(TimeStampedModel):
    """
    Missed bin collection report
    """
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return u"Missed Bin collection"

    def save(self, *args, **kwargs):
        super(Missed, self).save(args, kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse("collection:list")
