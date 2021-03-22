from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from student.views import router as student_router
from employee.views import router as employee_router

api = NinjaAPI()
api.add_router("",student_router)
api.add_router("",employee_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),
]
