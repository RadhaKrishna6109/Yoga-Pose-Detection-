"""yoga_pose_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as view
from users import views as users
from admins import views as admins

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name='index'),
    path('logout/', view.logout, name='logout'),


    path('UserLogin/', users.UserLogin, name='UserLogin'),
    path('UserHome/', users.userHome, name='UserHome'),
    path('UserRegisterAction/', users.UserRegisterAction, name='UserRegisterAction'),
    path('UserLoginCheck/', users.UserLoginCheck, name='UserLoginCheck'),
    path('train/', users.training_view, name='train'),
    path('UserTraining/', users.UserTraining, name='UserTraining'),
    path('prediction/', users.prediction_view, name='prod'),

    path('AdminLogin/', admins.AdminLogin, name='AdminLogin'),
    path('adminHome/', admins.AdminHome, name='adminHome'),
    path('AdminLoginCheck/', admins.AdminLoginCheck, name='AdminLoginCheck'),
    path('RegisterUsersView/', admins.RegisterUsersView, name='RegisterUsersView'),
    path('ActivaUsers/', admins.ActivaUsers, name='ActivaUsers'),



    # path('train_prediction/', include('yoga_train_pred.urls')),  
]
