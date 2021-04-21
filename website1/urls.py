from django.urls import path

from . import views


urlpatterns = [
    path('itdept', views.itdept, name='itdept'),
    path('compsdept', views.compsdept, name='compsdept'),
    path('mechdept', views.mechdept, name='mechdept'),
    path('extcdept', views.extcdept, name='extcdept'),
    path('dataentry', views.dataentry, name='dataentry'),
    path('login', views.signin, name='login'),
    path('signup', views.registration_view, name='signup')
]