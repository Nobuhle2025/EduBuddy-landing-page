from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('login/', views.login_view, name='login'),
     path('register/', views.register_view, name='register'),
     path('dashboard/', views.dashboard_view, name='dashboard'),
     path('logout/', views.logout_view, name='logout'),
     path('edit_assignment/<int:pk>/', views.edit_assignment, name='edit_assignment'),
    path('assignments/', views.assignments_view, name='assignments'),
     path('class_schedule/', views.class_schedule_view, name='class_schedule'),
    path('set_reminder/', views.set_reminder, name='set_reminder'),
    path('delete_assignment/<int:id>/', views.delete_assignment, name='delete_assignment'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
]


