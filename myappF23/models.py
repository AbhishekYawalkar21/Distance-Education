import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    STUDENT_STATUS_CHOICES = [('ER', 'Enrolled'),
                              ('SP', 'Suspended'),
                              ('GD', 'Graduated')]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    status = models.CharField(max_length=10, choices=STUDENT_STATUS_CHOICES, default='Enrolled')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    COURSE_LEVEL_CHOICES = [('BE', 'Beginner'),
                            ('IN', 'Intermediate'),
                            ('AD', 'Advanced')]
    level = models.CharField(max_length=10, choices=COURSE_LEVEL_CHOICES, default='Beginner')
    interested = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ORDER_STATUS_CHOICE = [(0, 'Order Confirmed'), (1, 'Order Cancelled')]
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICE, default=1)
    order_date = models.DateField()
    order_price = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    levels = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.student)

    def discount(self):
        if self.order_price is not None:
            self.order_price = self.order_price - (self.order_price / 10)
            return self.order_price
        return None
