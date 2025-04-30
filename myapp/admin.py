# admin.py
from django.contrib import admin
from .models import User, Course, Lesson, Task, Submission, Enrollment

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Task)
admin.site.register(Submission)
admin.site.register(Enrollment)