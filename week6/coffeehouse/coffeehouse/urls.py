"""coffeehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from menu.views import IndexView, ProfileUpdateView, SpecialUpdateView, SpecialDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name="profile_view"),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^special/(?P<pk>\d+)/update/$', SpecialUpdateView.as_view(), name="special_update_view"),
    url(r'^special/(?P<pk>\d+)/delete/$', SpecialDeleteView.as_view(), name="special_delete_view"),

]
