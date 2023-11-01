from django.urls import path
from myappF23 import views

app_name = 'myappF23'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:category_no>/', views.detail, name='detail'),
    path('course-description/<int:ins_id>/', views.ins_course_stud, name='ins_course_stud')
]