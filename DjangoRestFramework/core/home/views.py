from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framwork.views import APIView

@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)

    return Response({'status': 200, "payload": serializer.data})

@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403, 'message': "Something went wrong!"})
    serializer.save()
    return Response({'status': 200, "payload": serializer.data, 'message':'success'})

@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj, data=request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'message': "Something went wrong!"})
        serializer.save()
        return Response({'status': 200, "payload": serializer.data, 'message':'success'})
    except Exception as e:
        print(e)
        return Response({'status':403, 'message': 'invalid id'})
    
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status': 200, 'message':'deleted'})
    except Exception as e:
        print(e)
        return Response({'status':403, 'message': 'invalid id'})

@api_view(['GET'])
def get_book(request):
    book_objs=Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({'status':403, 'payload': serializer.data})