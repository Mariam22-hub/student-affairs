# Generated by Django 4.0.4 on 2022-05-24 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Table', '0006_department_remove_student_st_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='st_birthdate',
            field=models.DateField(auto_now=True),
        ),
    ]
