from django.urls import reverse
from rest_framework import status
from ninjadjangoapp.models import Task
from ninjadjangoapp.tests.base import BaseTestCase


class UpdateTaskByIdTestCase(BaseTestCase):

    def setUp(self):

        super().setUp()

        self.task = Task.objects.create(
            title="Sample Task",
            description="This is a sample task",
            status="Pending",
            due_date="2024-12-31"
        )

        self.valid_url = reverse(self.get_test_path('update_task_by_id'), kwargs={'id': self.task.id})
        self.invalid_url = reverse(self.get_test_path('update_task_by_id'), kwargs={'id': 9999})

    def test_update_task_by_id_success(self):
        """
        測試成功根據 id 更新任務
        """

        updated_data = {
            "title": "Updated Task",
            "description": "This is the updated task",
            "status": "Done",
            "due_date": "2025-01-01"
        }

        response = self.client.put(self.valid_url, data=updated_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_task = response.json()['data']
        for field, value in updated_data.items():
            self.assertEqual(updated_task[field], value, msg=f"{field} 預期為 {value}，實際為 {updated_task[field]}")


    def test_update_task_by_id_wrong_id(self):

        """
        測試查詢不存在的任務 id
        """

        updated_data = {
            "title": "Updated Task",
            "description": "This is the updated task",
            "status": "Done",
            "due_date": "2025-01-01"
        }

        response = self.client.put(self.invalid_url, data=updated_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

