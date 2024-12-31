from django.http import HttpRequest, JsonResponse
from ninjadjangoapp.models import StatusType, Task
from ninjadjangoapp.schemas import CreateTaskRequest, UpdateTaskRequest
from ninjadjangoapp.serializers import TaskSerializer
from ninja import Body


def create_task(request: HttpRequest, body: CreateTaskRequest = Body(...)):
    """
    創建任務
    """

    title = body.title
    description = body.description
    status = body.status
    due_date = body.due_date

    new_task = Task(
        title=title,
        description=description,
        status=status,
        due_date=due_date,
    )
    new_task.save()

    serializer = TaskSerializer(new_task)
    return JsonResponse({"data": serializer.data}, status=200)


def get_task_by_id(request: HttpRequest, id: int):
    """
    根據任務 ID 查詢任務資訊
    """

    task = Task.objects.filter(id=id).first()
    if not task:
        return JsonResponse({
            "error": "Invalid Parameter Error",
            "message": f"Task {id} not found in database"
        }, status=400)

    serializer = TaskSerializer(task)
    return JsonResponse({"data": serializer.data}, status=200)



def get_all_tasks(request: HttpRequest):
    """
    查詢所有任務資訊
    """
    tasks = Task.objects.filter(status=StatusType.PENDING.value).order_by('id').all()
    serializer = TaskSerializer(tasks, many=True)

    return JsonResponse({"data": serializer.data}, status=200)



def update_task_by_id(request: HttpRequest, id: int, body: UpdateTaskRequest = Body(...)):
    """
    根據任務 ID 更新任務資訊
    """

    title = body.title
    description = body.description
    status = body.status
    due_date = body.due_date

    task = Task.objects.filter(id=id).first()
    if not task:
        return JsonResponse({
            "error": "Invalid Parameter Error",
            "message": f"Task {id} not found in database"
        }, status=400)
    
    if title:
        task.title = title
    if description:
        task.description = description
    if status:
        task.status = status
    if due_date:
        task.due_date = due_date
    
    task.save()

    serializer = TaskSerializer(task)
    return JsonResponse({"data": serializer.data}, status=200)



def delete_task_by_id(request: HttpRequest, id: int):
    """
    根據任務 ID 刪除任務資訊
    """

    task = Task.objects.filter(id=id).first()
    if not task:
        return JsonResponse({
            "error": "Invalid Parameter Error",
            "message": f"Task {id} not found in database"
        }, status=400)
    

    task.delete()

    return JsonResponse({}, status=200)