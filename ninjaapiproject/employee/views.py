from ninja import Router
from .models import Employee
router = Router()


@router.get("/employee",tags=['employee'],summary="get list of employees")
def employee_get(request):
    return {"data":"employee get"}


