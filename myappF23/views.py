from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from .models import Category, Course, Student, Instructor, Order
from .forms import InterestForm, OrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import timedelta, datetime
from django.urls import reverse

# Create your views here.
@login_required
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
    # return render(request, 'myappF23/index.html', {'category_list': category_list})

    # last_login_info = request.session.get('last_login_info')
    # if last_login_info:
    #     return HttpResponse(f'Your last login was: {last_login_info}')
    # else:
    #     return HttpResponse('Your last login was more than 5 minutes ago')

    user_visits = request.COOKIES.get('user_visits', 0)
    last_login_info = request.session.get('last_login_info')
    response = render(request, 'myappF23/index.html', {
        'category_list': category_list,
        'user_visits': user_visits,
        'about_visits': request.COOKIES.get('user_visits_about', 0),
        'last_login_info': last_login_info,
    })
    if 'user_visits' in request.COOKIES:
        user_visits = int(request.COOKIES['user_visits']) + 1
    else:
        user_visits = 1
    response.set_cookie('user_visits', user_visits, max_age=10)
    return response

@login_required
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
    # orders = Order.objects.all()
    # all_courses = Course.objects.all().order_by('id')
    # return render(request, 'myappF23/about.html', {'all_courses': all_courses})
    # return render(request, 'myappF23/about.html')

    user_visits_about = request.COOKIES.get('user_visits_about', 0)
    response = render(request, 'myappF23/about.html',
                      {'user_visits_about': user_visits_about})

    if 'user_visits_about' in request.COOKIES:
        user_visits_about = int(request.COOKIES['user_visits_about']) + 1
    else:
        user_visits_about = 1
    response.set_cookie('user_visits_about', user_visits_about,
                        max_age=10)
    return response

@login_required
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

@login_required
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

def courses(request):
    course_list = Course.objects.all().order_by('id')
    return render(request, 'myappF23/courses.html', {'course_list': course_list})

@login_required
def place_order(request):
    msg = ''
    course_list = Course.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.course.level == 'BE':
                order.course.level = 1
            elif order.course.level == 'IN':
                order.course.level = 2
            elif order.course.level == 'AD':
                order.course.level = 3
            if order.levels > order.course.level:
                msg = 'You exceeded the number of levels for this course.'
                return render(request, 'myappF23/order_response.html', {'msg': msg})
            if order.course.price > 150.00:
                order.discount()
            order.save()
            msg = 'Your course has been ordered successfully.'
        else:
            msg = 'There was an issue with the form submission. Please check your input.'
            return render(request, 'myappF23/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myappF23/placeorder.html', {'form': form, 'msg': msg, 'course_list': course_list})

@login_required
def coursedetail(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interested = form.cleaned_data['interested']
            if interested == '1':
                course.interested += 1
                course.save()
                return redirect('myappF23:index')
    else:
        form = InterestForm(initial={'levels': 1})

    return render(request, 'myappF23/coursedetail.html', {'course': course, 'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['last_login_info'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                request.session.set_expiry(300)
                return HttpResponseRedirect(reverse('myappF23:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myappF23/login.html')

@login_required
def user_logout(request):
    # logout(request)
    request.session.flush()
    return HttpResponseRedirect(reverse('myappF23:index'))

@login_required
def myaccount(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'student'):
            student = request.user.student
            first_name = student.first_name
            last_name = student.last_name
            courses_ordered = Order.objects.filter(student=student, order_status=0)
            courses_interested = student.course_set.all()

            return render(request,'myappF23/myaccount.html', {
                'full_name': f"{first_name} {last_name}",
                'courses_ordered': courses_ordered,
                'courses_interested':courses_interested,
            })
        else:
            return HttpResponse('You are not a registered student!')
    else:
        return HttpResponse('You are not logged in!')

def set_test_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("Test cookie set")
    # response = HttpResponse("Test cookie set")
    # response.set_cookie('cookie1', '1')
    # return response

def check_test_cookie(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return HttpResponse('Test cookie worked')
    else:
        return HttpResponse('Test cookie failed')


#Lab 9 answers for part 3:
# d. Make the user’s session cookies to expire when the user’s web browser is closed instead of 5 minutes.
# i) do you need to change anything in your view functions?
#Answer: No, we don't have to change anything in view functions.

# ii) what setting you use to do that?
#Answer: In settings.py file, add one line: SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#        This line will make sure user's session cookies expire if the web browser is closed.