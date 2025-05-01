from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course, Lesson, Task, Submission, Enrollment

# Пользователь
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)

# Курсы
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher')  # убрал 'created_at', если поля нет
    search_fields = ('title',)
    list_filter = ('teacher',)

# Уроки
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_course_title')  # заменили course на метод
    search_fields = ('title', 'course__title')
    list_filter = ('course',)

    def get_course_title(self, obj):
        return obj.course.title
    get_course_title.short_description = 'Course'

# Задания
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'deadline')
    search_fields = ('title', 'lesson__title')
    list_filter = ('lesson',)

# Отправленные задания
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('task', 'student', 'submitted_at', 'grade')
    search_fields = ('student__username', 'task__title')
    list_filter = ('task', 'grade')
    readonly_fields = ('submitted_at',)

# Записи на курсы
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    search_fields = ('student__username', 'course__title')
    list_filter = ('course',)
    readonly_fields = ('enrolled_at',)
