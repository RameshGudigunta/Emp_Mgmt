# Generated by Django 2.2.4 on 2019-08-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Dept_emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField()),
                ('dept_no', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=5)),
                ('hire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('salary', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
    ]
