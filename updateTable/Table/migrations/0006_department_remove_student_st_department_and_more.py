# Generated by Django 4.0.4 on 2022-05-24 01:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Table', '0005_alter_student_st_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=2)),
                ('dep_head', models.CharField(max_length=100)),
                ('dep_ID', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='st_department',
        ),
        migrations.AlterField(
            model_name='student',
            name='st_active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='st_level',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='st_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Table.department'),
        ),
    ]
