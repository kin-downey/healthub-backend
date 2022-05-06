from django.contrib import admin
from django.urls import path, include, re_path

from accounts.views import test

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', test),

]
