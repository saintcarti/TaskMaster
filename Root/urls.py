from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginView, name='login'),
    path('register/', views.registerView,name='register'),
    path('dashboard',views.dashboardView, name='dashboard'),
    path('index',views.indexView, name='index'),
    path('task', views.taskView, name='task'),
    path('detail',views.detailView, name='detail'),
    path('logout',views.logoutView,name='logout')
]