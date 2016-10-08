from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^addjob/$', views.addJob, name="addjob"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/',views.user_login,name="login"),
    url(r'^welcome/',views.welcome,name="welcome"),
    url(r'^logout/',views.user_logout,name="logout"),

]
