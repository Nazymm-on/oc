from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home_view, name='home'),

    # Курсы
    path('courses/', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    # Панели
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),

    # Регистрация / Вход / Выход
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Добавление уроков и заданий
    path('course/<int:course_id>/add_lesson/', views.add_lesson, name='add_lesson'),
    path('lesson/<int:lesson_id>/add_task/', views.add_task, name='add_task'),

    # Отправка задания
    path('task/<int:task_id>/submit/', views.submit_task, name='submit_task'),

    path('courses/', views.course_gallery, name='course_gallery'),
    path('courses/<str:course_name>/', views.course_video, name='course_video'),

    path('course/<int:course_id>/video/', views.course_video, name='course_video'),

    path('course/html/', views.html_page, name='html_page'),
    path('course/css/', views.css_page, name='css_page'),
    path('course/javascript/', views.javascript_page, name='javascript_page'),
    path('course/python/', views.python_page, name='python_page'),
    path('course/java/', views.java_page, name='java_page'),
    path('course/kotlin/', views.kotlin_page, name='kotlin_page'),

    path('profile/', views.student_profile, name='student_profile'),
]
