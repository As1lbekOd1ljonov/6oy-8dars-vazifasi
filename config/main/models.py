from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=500, verbose_name="Kursnomi ")

    def __str__(self):
        return self.name

    class  Meta:
        verbose_name_plural = "Kurslar "
        verbose_name = "Kurs "

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200, verbose_name="Dars nomi ")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name="Kurs nomi")
    date = models.DateField(null=True, blank=True, verbose_name="Dars sanasi")
    summary = models.TextField(verbose_name="Dars Haqida")
    views = models.IntegerField(verbose_name="Ko'rishlar soni")

    def __str__(self):
        return f"{self.lesson_name} {self.course} {self.date} {self.summary}{self.views}"

    class  Meta:
        verbose_name_plural = "Darslar "
        verbose_name = "Dars "


class Comment(models.Model):
    text = models.TextField(verbose_name="Dars haqida firkingizni qoldiring: ")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name_plural = "Commentlar "
        verbose_name = "Comment "