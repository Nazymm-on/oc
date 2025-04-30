from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, LessonForm, TaskForm
from .models import User, Course, Lesson, Enrollment, Task, Submission

# Главная страница
def home_view(request):
    return render(request, 'myapp/home.html')

# Регистрация — автоматически назначается роль student
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'
            user.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

# Вход с переадресацией по роли
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'student':
                return redirect('student_dashboard')
            else:
                return redirect('course_list')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

# Выход
def logout_view(request):
    logout(request)
    return redirect('login')

# Проверка на учителя
def is_teacher(user):
    return user.is_authenticated and user.role == 'teacher'

# Список курсов
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'myapp/course_list.html', {'courses': courses})

# Детали курса
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lesson_set.all()
    return render(request, 'myapp/course_detail.html', {'course': course, 'lessons': lessons})

# Панель студента
@login_required
def student_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'myapp/student_dashboard.html', {'enrollments': enrollments})

# Панель преподавателя
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'myapp/teacher_dashboard.html', {'courses': courses})

# Добавление урока
@user_passes_test(is_teacher)
def add_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect('teacher_dashboard')
    else:
        form = LessonForm()
    return render(request, 'myapp/add_lesson.html', {'form': form, 'course': course})

# Добавление задания
@user_passes_test(is_teacher)
def add_task(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, course__teacher=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.lesson = lesson
            task.save()
            return redirect('teacher_dashboard')
    else:
        form = TaskForm()
    return render(request, 'myapp/add_task.html', {'form': form, 'lesson': lesson})

# Отправка задания студентом
@login_required
def submit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Submission.objects.create(task=task, student=request.user, content=content)
        return redirect('student_dashboard')
    return render(request, 'myapp/submit_task.html', {'task': task})

# Галерея курсов
@login_required
def course_gallery(request):
    courses = Course.objects.all()
    return render(request, 'myapp/course_gallery.html', {'courses': courses})

# Страницы по каждому языку
def html_page(request):
    return render(request, 'myapp/courses/html.html')

def css_page(request):
    return render(request, 'myapp/courses/css.html')

def javascript_page(request):
    return render(request, 'myapp/courses/javascript.html')

def python_page(request):
    return render(request, 'myapp/courses/python.html')

def java_page(request):
    return render(request, 'myapp/courses/java.html')

def kotlin_page(request):
    return render(request, 'myapp/courses/kotlin.html')

# Профиль студента
@login_required
def student_profile(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'myapp/student_profile.html', {
        'enrollments': enrollments
    })

# Видео по курсу
@login_required
def course_video(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'myapp/course_video.html', {
        'course': course,
        'lessons': lessons
    })
