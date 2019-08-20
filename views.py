from django.http import HttpResponse
from django.shortcuts import render
from welcome.models import *
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, date
# import datetime
from django.views.decorators.csrf import csrf_exempt

today = date.today()

def add_employee(request):
	return render(request,'addemployee.html')

def create_employee(request):
	emp_nmbr=request.POST.get('t1')
	date_of_birth=request.POST.get('t2')
	first_name1=request.POST.get('t3')
	last_name1=request.POST.get('t4')
	gender1=request.POST.get('t5')
	hire_date1=request.POST.get('t6')
	dob_date = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
	hire_date = datetime.strptime(hire_date1, '%Y-%m-%d').date()
	emp=Employees(emp_no=emp_nmbr,birth_date=date_of_birth,first_name=first_name1,last_name=last_name1,gender=gender1,hire_date=hire_date1)
	emp.save()
	return HttpResponse("Employee created sucesfully")

# API to create a user
class EmployeeCreate(APIView):

	def post(self, request, format=None):
		dob_date = datetime.strptime(request.data['t2'], '%Y-%m-%d').date()
		hire_date = datetime.strptime(request.data['t6'], '%Y-%m-%d').date()
		request.data['t2'] = dob_date
		request.data['t6'] = hire_date
		serializer = serializers.EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			diff_years = today - dob_date
			age = str(int(str(diff_years).split(" ")[0])/365).split(".")[0]
			if age >=18 and age <=60:
				serializer.save()
			return Response("Employee Created Successfully")
		return Response(serializer.errors)

	def get(self, request):
		hike = True
		emp_no = request.GET['emp_no']
		employees = Employees.objects.filter(emp_no = emp_no)
		dept_empls = Dept_emp.objects.filter(emp_no = emp_no)
		dept_no = dept_empls[0].dept_no
		dept_names = Departments.objects.filter(dept_no=dept_no)
		dept_name = dept_names[0].dept_name
		titles = Titles.objects.filter(emp_no = emp_no)
		title = titles[0].title
		join_date = employees[0].hire_date
		birth_date = employees[0].birth_date
		gender = employees[0].gender
		diff_years_exp = today - join_date
		diff_years_age = today - birth_date
		experience = str(int(str(diff_years_exp).split(" ")[0])/365).split(".")[0]
		age = str(int(str(diff_years_age).split(" ")[0])/365).split(".")[0]

		if dept_name in ["Customer Service", "Development", "Finance", "Human Resources", "Human Resources","Sales"] or \
		   title in ["Senior Engineer", "Staff", "Engineer", "Senior Staff", "Assistant Engineer", "Technique Leader"] or \
		   experience <=1 or age <=20 or gender == "M" and title == "Technique Leader":
		   hike = False
		else:
			hike = hike
			# considering title as designation
		response = {"hike":hike, "designation":title}
		return Response(response)
	