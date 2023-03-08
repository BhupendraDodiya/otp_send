from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('reg/',views.registration),
    path('login/',views.login),
    path('log/',views.log),
    path('forget/',views.forget),
    path('gen/',views.generate_otp),
    path('otpver/',views.otpverify),
    path('verify/',views.verify),
    path('update/',views.update),
    path('check/',views.check),
]
