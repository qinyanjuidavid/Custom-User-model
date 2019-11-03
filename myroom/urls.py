from django.urls import path
from myroom import views
from django.contrib.auth import views as auth_view
app_name='myroom'

urlpatterns=[
path('',views.home,name='home'),

]
