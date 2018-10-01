from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.cur_time, name='time'),
    url(r'hello', views.hello, name='hello'),
    url(r'dashboard', views.dashboard, name='dashboard'),
    # url('accounts/', include('django.contrib.auth.urls')),
    # url('accounts/register/', views.SignUpView.as_view(), name='signup'),
    # url('accounts/register/patient/', views.PatientRegisterView.as_view(), name='patient_register'),
    # url('accounts/register/responder/', views.ResponderRegisterView.as_view(), name='responder_register')
]
