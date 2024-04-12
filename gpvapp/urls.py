from django.urls import path

from gpvapp import views

urlpatterns = [
    path('',views.home),
    path('marriagevalidator',views.marriage_fun),
    path('leapcheck',views.leap_fun),
]