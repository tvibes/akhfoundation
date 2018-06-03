from django.conf.urls import url
from . import views


# Site urls are in listed
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about-us/$', views.about_us, name='about_us'),
    url(r'^our-vision', views.vision, name='vision'),
    url(r'^ourmission/$', views.our_mission, name='our_mission'),
    url(r'^programs/youths-development/$', views.youths_empowerment, name='youths_empowerment'),
    url(r'^programs/healthcare/$', views.healthcare, name='healthcare'),
    url(r'^programs/peace-and-security/$', views.peace_and_security, name='peace_and_security'),
    url(r'^programs/educatioon-and-training/$', views.education_and_training, name='education_and_training'),
    url(r'^get-involved/donate/$', views.donate, name='donate')
 ]