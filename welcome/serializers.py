from welcome.models import *
from rest_framework import serializers
class EmployeeSerializer(serializers.Serializer):
	class Meta:
		model=Employees
		fields=['emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date']
    