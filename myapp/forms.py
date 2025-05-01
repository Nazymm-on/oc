from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Lesson, Task

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field_name.capitalize().replace("_", " ")
            }
)


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url']

    def clean_video_url(self):
        video_url = self.cleaned_data.get('video_url')
        if video_url and not video_url.startswith('https://'):
            return f'https://www.youtube.com/embed/{video_url}'
        return video_url


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
