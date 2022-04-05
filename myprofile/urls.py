from django.urls import path
from . import views

app_name='myprofile'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>',views.portfolio_details, name='portfolio_details'),
    #path('index', views.contact, name="contact"),
]
