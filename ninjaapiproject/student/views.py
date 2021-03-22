from ninja import Router, Schema
from .models import Student
from django.http import JsonResponse
from rest_framework import serializers

router = Router()


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StudentSchema(Schema):
    student_name : str
    student_roll_number : int
    student_marks : float

class StudentUpdateSchema(Schema):
    student_name : str = None
    student_roll_number : int = None
    student_marks : float = None




@router.get("/student",tags=['student'],summary="get list of students")
def student_get(request):
    stds = Student.objects.all()
    ser = StudentSerializer(stds,many=True).data
    return JsonResponse({"data":ser})

@router.post("/student",tags=['student'],summary="create a student")
def student_create(request,body : StudentSchema):
    body = body.dict()
    std = Student(
        sname = body['student_name'],
        sroll=body['student_roll_number'],
        smarks=body['student_marks']
    )
    std.save()
    ser = StudentSerializer(std)
    return JsonResponse({"status":"success","msg":"student created","data":ser.data},status=200)


@router.get("/student/{student_id}",tags=['student'],summary="get a student")
def student_get_partiular(request,student_id):
    try:
        std = Student.objects.get(id=student_id)
        ser = StudentSerializer(std)
        return JsonResponse({"status":"success","data":ser.data},status=200)
    except:
        return JsonResponse({"status":"failed","msg":"student not found"},status=404)


@router.delete("/student/{student_id}",tags=['student'],summary="delete a student")
def student_get_partiular(request,student_id):
    try:
        std = Student.objects.get(id=student_id)
        std.delete()
        return JsonResponse({"status":"success","msg":"student deleted"},status=200)
    except:
        return JsonResponse({"status":"failed","msg":"student not found"},status=404)
    
@router.put("/student/{student_id}",tags=['student'],summary="partial and full update of a student")
def student_update(request,student_id,body:StudentUpdateSchema):
    try:
        std = Student.objects.get(id=student_id)
        body = body.dict()
        print(body)
        if body.get("student_name"):
            std.sname = body.get("student_name")
        if body.get("student_roll_number"):
            std.sroll = body.get("student_roll_number")
        if body.get("student_marks"):
            std.smarks = body.get("student_marks")

        std.save()
        ser = StudentSerializer(std)
        return JsonResponse({"status":"success","msg":"student updated","data":ser.data},status=200)
    except Student.DoesNotExist:
        return JsonResponse({"status":"failed","msg":"student not foundsv"},status=404)