from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view,APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerailizer
from .models import Employee

# Create your views here.

def about(request):
    return HttpResponse("Good Morning")

def home(request):
    return HttpResponse("Welcome")

@api_view(['GET'])
def index(request):
    details={
        'name':'Greeshma',
        'age':40
    }
    return Response(details)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def employeedetails(request):
    if request.method == 'GET':
        # Retrieve all Person objects
        employeeobj=Employee.objects.all()
        serializer = EmployeeSerailizer(employeeobj,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # Create a new Person object
        employeedata=request.data
        serializer=EmployeeSerailizer(data=employeedata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    elif request.method == 'PUT':
        # Update an existing Person object
        data=request.data
        try:
            employeeobj=Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error":"Employee not found"},status=404)
        
        serializer = EmployeeSerailizer(employeeobj,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    elif request.method == 'PATCH':
        # Partially update an existing Person object
        data=request.data
        try:
            employeeobj=Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error":"Employee not found"},status=404)
        
        serializer = EmployeeSerailizer(employeeobj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    elif request.method == 'DELETE':
        # Delete a Person object
        data=request.data
        try:
            employeeobj=Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error":"Employee not found"},status=404)
        employeeobj.delete()
        return Response({"message": "Person deleted successfully"}, status=204)


# Class Based

class EmployeeView(APIView):
    def get(self,request):
        employeeobj=Employee.objects.all()
        serializer = EmployeeSerailizer(employeeobj,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=EmployeeSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        try:
            employeedata=Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
             return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerailizer(employeedata,data=request.data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            employeedata=Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
             return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerailizer(employeedata,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(Self,request):
        try:
            employeedata=Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        employeedata.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Using ModelViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset =Employee.objects.all() # Define the queryset for the viewset
    serializer_class=EmployeeSerailizer # Specify the serializer to be used
