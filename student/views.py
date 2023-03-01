from django.shortcuts import render
from django.http import HttpResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# def index(request):
#     return HttpResponse("student page")
@api_view(['POST'])
def add_student(request):
    try:
        params=request.data
        serialised_data=StudentSerializer(data=params)
        if serialised_data.is_valid():
            serialised_data.save()
            return Response({'msg':'student added','status code':201})
        else:
            return Response({'msg':'form error','status code':403})
    except:
            return Response({'msg':'something went wrong......','status code':500})
        
          
@api_view(['GET'])
def view_student(request):
    student_data=Student.objects.all()
    serialised_data=StudentSerializer(student_data,many=True)
    return Response({'students':serialised_data.data})
    
@api_view(['PUT'])
def update_student(request,stud_id):
    params=request.data
    try:
        stud_data=Student.objects.get(id=stud_id)
        serialised_data=StudentSerializer(stud_data,data=params)
        if serialised_data.is_valid():
                serialised_data.save()
                return Response({'msg':'student data updated','status code':203})
        else:
                print(serialised_data.errors)
                return Response({'msg':'form error','status code':403})
    except:
         return Response({'msg':'student not found','status code':404})

@api_view(['DELETE'])
def delete_student(request,stud_id):
    try:
        stude_data=Student.objects.get(id=stud_id)
        stude_data.delete()
        return Response({'msg':'deleted student','status code':202})
    except:
        return Response({'msg':'student not found','status code':404})