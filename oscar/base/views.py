# -*- coding: utf-8 -*-
# Created on 21 Apr 2016 at 11:08
from __future__ import unicode_literals, absolute_import
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse


class HomepageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            url = reverse("collection:list")
        else:
            url = reverse("account_login")

        return url
