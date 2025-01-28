from django.urls import path
from . import views

urlpatterns = [
    path('',views.home1),
    path('login',views.login),
    path('log',views.log),
    path('doctor_login',views.doctor_login),
    path('doctor_log',views.doctor_log),
    path('home1',views.home1),
    path('index',views.index),
    path('signup1',views.signup1),
    path('sign',views.sign),
    path('booking',views.booking),
    
    path('admin_login',views.admin_login),
    path('admin_signup',views.admin_signup),
    path('admin_sign',views.admin_sign),
    path('admin_log',views.admin_log),
    path('admin_dash',views.admin_dash),
    path('dashedit/<int:id>',views.dashedit),
    path('dele/<int:id>',views.dele),
    path('edit/<int:id>',views.edit),
    path('after_login',views.after_login),
    path('admin_page',views.admin_page),
    path('user_account',views.user_account),
    path('About',views.About),
    path('doctor_login',views.doctor_login),
    path('doctor_dash/<str:name>',views.doctor_dash),
    path('doc_page',views.doc_page),
    path('docreg',views.docreg),
    path('docregcode',views.docregcode),
]
