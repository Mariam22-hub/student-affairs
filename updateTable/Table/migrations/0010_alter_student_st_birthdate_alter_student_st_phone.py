# Generated by Django 4.0.4 on 2022-05-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Table', '0009_remove_student_st_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='st_birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='st_phone',
            field=models.CharField(max_length=15),
        ),
    ]
