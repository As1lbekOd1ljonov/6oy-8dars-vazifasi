from django import forms
from .models import Course, Lesson, Comment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
        labels = {
            'name': 'Kurs nomi'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LessonForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Kursni tanlang",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Lesson
        fields = ['lesson_name', 'course', 'date', 'summary', 'views']
        labels = {
            'lesson_name': 'Dars mavzusi',
            'course': 'Kurs nomi',
            'date': 'Kategoriya',
            'summary': 'Dars haqida',

        }
        widgets = {
            'lesson_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    widgets = {
        'text': forms.TextInput(attrs={'class': 'form-control'}),
    }