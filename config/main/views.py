from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Comment
from .form import CourseForm, LessonForm, CommentFrom
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def index(request):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    return render(request, 'index.html', {'courses': courses, 'lessons': lessons})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    comments = Comment.objects.filter(lesson=lesson)
    if request.method == "POST":
        form = CommentFrom(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.lesson = lesson
            comment.user = request.user
            comment.save()
            messages.success(request, "Fikr qoldirildi!")
            return redirect('lesson_detail', lesson_id=lesson.id)
    else:
        form = CommentFrom()
    return render(request, 'lesson_detail.html', {'lesson': lesson, 'comments': comments, 'form': form})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Yangi kurs qo‘shildi!")
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def add_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            messages.success(request, "Yangi dars qo‘shildi!")
            return redirect('course_detail', course_id=course.id)
    else:
        form = LessonForm()
    return render(request, 'add_lesson.html', {'form': form, 'course': course})

def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Kurs yangilandi!")
            return redirect('index')
    else:
        form = CourseForm(instance=course)
    return render(request, 'update_course.html', {'form': form})


def update_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, "Dars yangilandi!")
            return redirect('index')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'update_lesson.html', {'form': form})



def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    messages.success(request, "Kurs o‘chirildi!")
    return redirect('index')

def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    lesson.delete()
    messages.success(request, "Dars o‘chirildi!")
    return redirect('index')

def delete_comment(request, lesson_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if  request.user == comment.user or request.user.is_staff:
        comment.delete()
        return redirect("lesson_detail", lesson_id)
    else:

        return redirect("lesson_detail", lesson_id)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Hush kelibsiz {user.username}!")
            return redirect('index')
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri!")

    return render(request, 'user_login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            messages.success(request, "Akount muofiqiyatli qo'shildi !\n"
                                      "Iltimos login qiling !")
        return redirect("user_login")
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    messages.warning(request, "Siz akoutni tark etingiz !")
    return redirect("user_login")

