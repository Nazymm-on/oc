# views.py
from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Enrollment
from django.contrib.auth.decorators import login_required

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lesson_set.all()
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})

@login_required
def student_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'student_dashboard.html', {'enrollments': enrollments})