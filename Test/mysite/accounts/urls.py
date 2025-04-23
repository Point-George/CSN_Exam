from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_account, name='create_account'),
    path('', views.login_account, name='login_account'),

]
#path('exam/', views.Exam_booking, name='Exam_booking'),