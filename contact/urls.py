from django.urls import path
from . import views
from .views import Person


app_name = 'contact'


urlpatterns = [
    path('', views.contact_new, name='contact_list'),
#	path('', views.Person, name='Person'),

]