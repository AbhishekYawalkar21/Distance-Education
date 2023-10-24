from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Course, Student, Instructor

# Create your views here.
def index(request):
    # category_list = Category.objects.all().order_by('id')[:10]
    # response = HttpResponse()
    # heading1 = '<h2>' + 'List of Categories:' + '</h2>'
    # response.write(heading1)
    # for category in category_list:
    #     para = '<p>' + str(category) + '</p>'
    #     response.write(para)
    # return response

    course_list = Course.objects.all().order_by('-price')[:5]
    response = HttpResponse()
    heading1 = '<h2>' + 'List of Courses:' + '</h2>'
    response.write(heading1)
    for course in course_list:
        para = '<p>' + str(course) + '</p>'
        response.write(para)
    return response

def about(request):
    response = HttpResponse()
    text1 = '<h1>' + 'This is a Distance Education Website! Search our Categories to find all available Courses.' + '</h1>'
    response.write(text1)
    return response

def detail(request, category_no):
    get_object_or_404(Category, id=category_no)
    category = Category.objects.get(id=category_no)
    courses = category.course_set.all()
    response = HttpResponse()
    category_name = '<h1>' + str(category) + '</h1>'
    response.write(category_name)
    heading2 = '<h2>' + 'Courses:' + '</h2>'
    response.write(heading2)
    for course in courses:
        list_of_courses = '<li>' + str(course) + '</li>'
        response.write(list_of_courses)
    return response
