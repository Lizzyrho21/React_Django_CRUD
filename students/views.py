from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Student
from .serializers import *

#using funciton based views here, so we use the @api_view decorator and specify the HTTP methods!

# Gets all students

#We want to READ/+1 and CREATE with this view
@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        #gets data in our db object
        data = Student.objects.all()

            #translate our model data into a JSON ready package
        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        # translates our created data into JSON
        serializer = StudentSerializer(data=request.data)
        #If all fields are filled correctly, the data will save
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#For update and Delete
@api_view(['PUT', 'DELETE'])
def students_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
