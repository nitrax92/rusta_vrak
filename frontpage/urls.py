from django.conf.urls import url
from . import views

app_name='frontpage'
urlpatterns = [
    url('^bil/$', views.search_function, name='search_funciton')
]