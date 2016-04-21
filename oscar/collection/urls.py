from django.conf.urls import url

from .views import MissedListView, MissedCreateView

urlpatterns = [
    url(r'^$', MissedListView.as_view(), name='list'),
    url(r'^create/?$', MissedCreateView.as_view(), name='create'),
]
