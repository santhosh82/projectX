from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^addjob/$', views.addJob, name="addjob"),
    url(r'^deletejob/(?P<id>[0-9]+)$', views.deleteJob, name="deletejob"),
    url(r'^register/$', views.register, name="register"),
    url(r'^welcome/', views.welcome, name="welcome"),
    url(r'^about/', views.about, name="about"),
    url(r'^logout/', views.user_logout, name="logout"),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^getjobslist/$', views.jobs_list, name="getjobslist"),
    url(r'^editjob/(?P<myId>[0-9]+)$',views.editJob, name="editjob"),
    url(r'^sanportfolio/$', views.san_portfolio, name="sanportfolio"),
    url(r'^addfriends/$',views.add_friends,name = "addfriends"),

    url(r'^makefriends/$',views.make_friends, name = "makefriends"),
    url(r'^sharejob/(?P<myId>[0-9]+)/$', views.share_job, name="sharejob"),

    # url to add jobs to job shared table
    url(r'^addjobshare/$',views.add_job_share, name="addjobshare"),

    # url to get the list of shared jobs to a user
    url(r'^getsharedlist/$',views.get_shared_list,name="getsharedlist"),




    url(r'^api/getusers/(?P<partialName>[a-zA-Z0-9]+)/$',views.get_users,name="getusers"),



    url(r'^editjob/', views.dummy ,name="tempeditjob"),
    url(r'^deletejob/',views.dummy,name="tempdeletejob"),
    #url(r'^getjobsshared/$', views.jobs_shared_list,name="getjobsshared")

]
