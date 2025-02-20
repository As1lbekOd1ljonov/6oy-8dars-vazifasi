from django.urls import path
from .views import (index, course_detail, lesson_detail, add_course, add_lesson,
    update_course, update_lesson, delete_course, delete_lesson, delete_comment, user_login, user_logout, user_register)

urlpatterns = [
    path('', index, name='index'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),

    path('add_course/', add_course, name='add_course'),
    path('add_lesson/<int:course_id>/', add_lesson, name='add_lesson'),

    path('update_course/<int:course_id>/', update_course, name='update_course'),
    path('update_lesson/<int:lesson_id>/', update_lesson, name='update_lesson'),

    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),
    path('delete_lesson/<int:lesson_id>/', delete_lesson, name='delete_lesson'),

    path('lesson/<int:lesson_id>/comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),

    path('user_login/', user_login, name='user_login'),
    path('user_register/', user_register, name='user_register'),
    path('user_logout/', user_logout, name='user_logout'),
]