from django.contrib.auth.models import AbstractUser
from django.db import models

# Пользователь с ролью
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

# Курс
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    created_at = models.DateTimeField(auto_now_add=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)  # Можно использовать как общее видео курса

    def __str__(self):
        return self.title

# Урок
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_embed_url(self):
        if self.video_url:
            if "watch?v=" in self.video_url:
                video_id = self.video_url.split("watch?v=")[-1]
            elif "youtu.be/" in self.video_url:
                video_id = self.video_url.split("youtu.be/")[-1]
            else:
                return ""
            return f"https://www.youtube.com/embed/{video_id}"
        return ""

    def __str__(self):
        return self.title

# Задание
class Task(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

# Отправка задания студентом
class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    content = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=5, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.username} → {self.task.title}"

# Запись на курс
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} ↔ {self.course.title}"
