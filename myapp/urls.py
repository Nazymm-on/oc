from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('course/<int:course_id>/add_lesson/', views.add_lesson, name='add_lesson'),

]
