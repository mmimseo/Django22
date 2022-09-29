from django.urls import path
from . import views

urlpatterns = [ # IP주소/blog/
    path('', views.landing), # IP주소/blog/
    path('about_me/', views.about_me) # IP주소/about_me/

]