from django.http import HttpResponse
from django.shortcuts import render
from welcome.models import *
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, date
# import datetime
from django.views.decorators.csrf import csrf_exempt



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
		today = date.today()
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
