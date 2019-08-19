from django.db import models
class Employees(models.Model):
	emp_no=models.IntegerField(primary_key=True)
	birth_date=models.DateField()
	first_name=models.CharField(max_length=14)
	last_name=models.CharField(max_length=16)
	gender=models.CharField(max_length=5)
	hire_date=models.DateField()
	def __str__(self):
		return self.first_name
		

class Departments(models.Model):
	dept_no=models.IntegerField(primary_key=True)
	dept_name=models.CharField(max_length=40)

class Dept_emp(models.Model):
	emp_no=models.IntegerField()
	dept_no=models.IntegerField()
	from_date=models.DateField()
	to_date=models.DateField()

class Titles(models.Model):
	emp_no=models.IntegerField()
	title=models.CharField(max_length=50)
	from_date=models.DateField()
	to_date=models.DateField()

class Salaries(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    salary=models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()	




