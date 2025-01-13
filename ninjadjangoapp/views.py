from django.http import HttpRequest, JsonResponse
from ninjadjangoapp.models import Task
from ninjadjangoapp.schemas import CreateTaskRequest, UpdateTaskRequest
from ninjadjangoapp.serializers import TaskSerializer
from ninja import Body
from rest_framework import status as http_status


def create_task(request: HttpRequest, body: CreateTaskRequest = Body(...)):
    """
    創建任務
    """

    title = body.title
    description = body.description
    status = body.status
    due_date = body.due_date

    if not title or title == '':
        return JsonResponse({
            "error": "Invalid Parameter Error",
            "message": f"Parameter title should not be empty in request body."
        }, status=http_status.HTTP_400_BAD_REQUEST)

    new_task = Task(
        title=title,
        description=description,
        status=status,
        due_date=due_date,
    )
    new_task.save()

    serializer = TaskSerializer(new_task)
    return JsonResponse({"data": serializer.data}, status=http_status.HTTP_200_OK)


def get_task_by_id(request: HttpRequest, id: int):
    """
    根據任務 id 查詢任務資訊
    """

    task = Task.objects.filter(id=id).first()
    if not task:
        return JsonResponse({
            "error": "Invalid Parameter Error",
            "message": f"Task {id} not found in database"
        }, status=http_status.HTTP_400_BAD_REQUEST)

    serializer = TaskSerializer(task)
    return JsonResponse({"data": serializer.data}, status=http_status.HTTP_200_OK)



def get_all_tasks(request: HttpRequest):
    """
    查詢所有任務資訊
    """

    tasks = Task.objects.order_by('id').all()
    serializer = TaskSerializer(tasks, many=True)

    return JsonResponse({"data": serializer.data}, status=http_status.HTTP_200_OK)



def update_task_by_id(request: HttpRequest, id: int, body: UpdateTaskRequest = Body(...)):
    """
    根據任務 id 更新任務資訊
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
        }, status=http_status.HTTP_400_BAD_REQUEST)
    
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
    return JsonResponse({"data": serializer.data}, status=http_status.HTTP_200_OK)



def delete_task_by_id(request: HttpRequest, id: int):
    """
    根據任務 id 刪除任務資訊
    """

    task = Task.objects.filter(id=id).first()
    if not task:
        return JsonResponse({
            "error": "Invalid Parameter Error",
            "message": f"Task {id} not found in database"
        }, status=http_status.HTTP_400_BAD_REQUEST)
    

    task.delete()

    return JsonResponse({}, status=http_status.HTTP_200_OK)