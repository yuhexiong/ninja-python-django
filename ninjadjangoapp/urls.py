from ninja import Router
from ninjadjangoapp import views
from ninjadjangoapp.schemas import BaseResponse, TaskDataResponse


router = Router()


router.api_operation(
    methods=["POST"], path="/task", response=TaskDataResponse,
    summary="create task", tags=["Task"],
)(views.create_task)

router.api_operation(
    methods=["GET"], path="/task/{int:id}", response=BaseResponse,
    summary="get task by id", tags=["Task"],
)(views.get_task_by_id)

router.api_operation(
    methods=["GET"], path="/tasks", response=BaseResponse,
    summary="get all tasks", tags=["Task"],
)(views.get_all_tasks)

router.api_operation(
    methods=["PUT"], path="/task/{int:id}", response=TaskDataResponse,
    summary="update task by id", tags=["Task"],
)(views.update_task_by_id)

router.api_operation(
    methods=["DELETE"], path="/task/{int:id}", response=BaseResponse,
    summary="delete task by id", tags=["Task"],
)(views.delete_task_by_id)