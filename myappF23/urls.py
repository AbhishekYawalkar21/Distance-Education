from django.urls import path
from myappF23 import views

app_name = 'myappF23'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:category_no>/', views.detail, name='detail'),
    path('course-description/<int:ins_id>/', views.ins_course_stud, name='ins_course_stud'),
    path('courses/', views.courses, name='courses'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_response/', views.place_order, name='order_response'),
    path('courses/<int:course_id>', views.coursedetail, name='coursedetail'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('set-cookie/', views.set_test_cookie, name='set_test_cookie'),
    path('check-cookie/', views.check_test_cookie, name='check_test_cookie')
]