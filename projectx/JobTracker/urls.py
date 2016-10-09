from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^addjob/$', views.addJob, name="addjob"),
    url(r'^register/$', views.register, name="register"),
    url(r'^welcome/',views.welcome,name="welcome"),
    url(r'^logout/',views.user_logout,name="logout"),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^getjobslist/$', views.jobs_list, name="getjobslist"),
    #url(r'^getjobsshared/$', views.jobs_shared_list,name="getjobsshared")

]
