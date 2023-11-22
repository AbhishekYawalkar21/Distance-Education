# Generated by Django 5.0b1 on 2023-11-21 22:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('level', models.CharField(choices=[('BE', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced')], default='Beginner', max_length=10)),
                ('interested', models.PositiveIntegerField(default=1)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappF23.category')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappF23.instructor')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('date_of_birth', models.DateField()),
                ('status', models.CharField(choices=[('ER', 'Enrolled'), ('SP', 'Suspended'), ('GD', 'Graduated')], default='Enrolled', max_length=10)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.IntegerField(choices=[(0, 'Order Confirmed'), (1, 'Order Cancelled')], default=1)),
                ('order_date', models.DateField()),
                ('order_price', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('levels', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappF23.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappF23.student')),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='students',
            field=models.ManyToManyField(to='myappF23.student'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='myappF23.student'),
        ),
    ]
