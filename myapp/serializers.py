# serializers.py
from rest_framework import serializers
from .models import User, Course, Lesson, Task, Submission, Enrollment


# Сериализатор для модели User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


# Сериализатор для модели Course
class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()  # Включаем данные преподавателя

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'created_at', 'video_url']


# Сериализатор для модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()  # Включаем данные курса

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'video_url', 'lab_description', 'created_at']


# Сериализатор для модели Task
class TaskSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()  # Включаем данные урока

    class Meta:
        model = Task
        fields = ['id', 'lesson', 'title', 'description', 'deadline']


# Сериализатор для модели Submission
class SubmissionSerializer(serializers.ModelSerializer):
    task = TaskSerializer()  # Включаем данные задания
    student = UserSerializer()  # Включаем данные студента

    class Meta:
        model = Submission
        fields = ['id', 'task', 'student', 'content', 'submitted_at', 'grade', 'feedback']


# Сериализатор для модели Enrollment
class EnrollmentSerializer(serializers.ModelSerializer):
    student = UserSerializer()  # Включаем данные студента
    course = CourseSerializer()  # Включаем данные курса

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at']
