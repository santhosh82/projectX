from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^addjob/$', views.addJob, name="addjob"),
    url(r'^deletejob/(?P<id>[0-9]+)/$', views.deleteJob, name="deletejob"),
    url(r'^register/$', views.register, name="register"),
    url(r'^welcome/', views.welcome, name="welcome"),
    url(r'^about/', views.about, name="about"),
    url(r'^logout/', views.user_logout, name="logout"),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^getjobslist/$', views.jobs_list, name="getjobslist")

]
