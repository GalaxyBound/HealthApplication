from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'hello', views.hello, name='hello'),
    url(r'dashboard', views.dashboard, name='dashboard'),
    url(r'index', views.index, name='index'),
    url(r'map', views.map, name='map'),
    url(r'login', views.signin, name='signin'),
    url(r'help', views.help, name='help'),
    url(r'signup/patient', views.signup_patient, name='signup_patient'),
    url(r'signup/responder', views.signup_responder, name='signup_responder'),
    url(r'signup/confirm', views.signup_confirm, name='signup_confirm'),
    url(r'signup', views.signup, name='signup'),
    url(r'test', views.test_post, name='test_post'),
    # url('accounts/', include('django.contrib.auth.urls')),
    # url('accounts/register/', views.SignUpView.as_view(), name='signup'),
    # url('accounts/register/patient/', views.PatientRegisterView.as_view(), name='patient_register'),
    # url('accounts/register/responder/', views.ResponderRegisterView.as_view(), name='responder_register')
]
