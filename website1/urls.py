from django.urls import path

from . import views


urlpatterns = [
	path('', views.home, name = 'home'),
    path('itdept', views.itdept, name='itdept'),
    path('compsdept', views.compsdept, name='compsdept'),
    path('mechdept', views.mechdept, name='mechdept'),
    path('extcdept', views.extcdept, name='extcdept'),
    path('dataentry', views.dataentry, name='dataentry'),
    path('editdata', views.edit_data, name='editdata')
]