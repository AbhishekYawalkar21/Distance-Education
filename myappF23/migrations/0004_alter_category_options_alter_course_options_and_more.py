# Generated by Django 4.2.6 on 2023-10-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappF23', '0003_instructor_students'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterField(
            model_name='instructor',
            name='students',
            field=models.ManyToManyField(to='myappF23.student'),
        ),
    ]
