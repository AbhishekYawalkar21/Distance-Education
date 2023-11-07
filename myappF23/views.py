from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Course, Student, Instructor

# Create your views here.
def index(request):
    # with HttpResponse
    # category_list = Category.objects.all().order_by('id')[:10]
    # response = HttpResponse()
    # heading1 = '<h2>' + 'List of Categories:' + '</h2>'
    # response.write(heading1)
    # for category in category_list:
    #     para = '<li>' + str(category) + '</li>'
    #     response.write(para)
    #
    # course_list = Course.objects.all().order_by('-price')[:5]
    # heading1 = '<h2>' + 'List of Courses:' + '</h2>'
    # response.write(heading1)
    # for course in course_list:
    #     para = '<li>' + str(course) + ': ' + str(course.price) + '</li>'
    #     response.write(para)
    # return response

    # with render
    category_list = Category.objects.all().order_by('id')[:10]
    return render(request, 'myappF23/index.html', {'category_list': category_list})

def about(request):
    # with HttpResponse
    # response = HttpResponse()
    # text1 = '<h1>' + 'Course name:' + '</h1>'
    # response.write(text1)
    # course = Course.objects.get(id=1)
    # course_name = '<h2>' + str(course) + '</h2>'
    # response.write(course_name)
    #
    # students = course.students.all()
    # text2 = '<h1>' + 'All Students:' + '</h1>'
    # response.write(text2)
    # for student in students:
    #     s = '<li>' + str(student) + '</li>'
    #     response.write(s)
    # return response

    # With render
    return render(request, 'myappF23/about.html')

def detail(request, category_no):
    # With Http Response
    # get_object_or_404(Category, id=category_no)
    # category = Category.objects.get(id=category_no)
    # courses = category.course_set.all()
    # response = HttpResponse()
    # category_name = '<h1>' + str(category) + '</h1>'
    # response.write(category_name)
    # heading2 = '<h2>' + 'Courses:' + '</h2>'
    # response.write(heading2)
    # for course in courses:
    #     list_of_courses = '<li>' + str(course) + '</li>'
    #     response.write(list_of_courses)
    # return response

    # With Render
    category = get_object_or_404(Category, pk=category_no)
    courses = category.course_set.all()
    categories_courses = {
        'category': category,
        'courses': courses,
    }
    return render(request, 'myappF23/detail.html', {'categories_courses': categories_courses})

def ins_course_stud(request, ins_id):
    course = Course.objects.get(id=ins_id)
    instructor = course.instructor.first_name + ' ' + course.instructor.last_name
    students = course.students.all()
    context = {
        'instructor': instructor,
        'students': students,
        'course': course,
    }
    return render(request, 'myappF23/course_details.html', {'context': context})
