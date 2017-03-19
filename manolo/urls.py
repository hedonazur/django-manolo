# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from visitors import views
from api.views import schema_view


urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^administramelo/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^search_date/$', views.search_date),
    url(r'^search/', views.search, name='search_view'),
    url(r'^create_alert/', views.create_alert, name='create_alert'),
    url(r'^api/', include('api.urls')),
    url(r'^docs/', schema_view),
    url(r'^about/', views.about, name='about'),
    url(r'^', include('visitors.urls', namespace="visitors")),
    url(r'robots.txt$', views.robots, name='robots'),
    url(r'^cazador/', include('cazador.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO: rewrite build_page method of haystack.views SearchView to
# produce a nicer pagination that includes max 20 pages to click
