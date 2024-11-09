from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.landing_page, name='land'),
    path('subs/', views.submitMail, name='submitMail')

]