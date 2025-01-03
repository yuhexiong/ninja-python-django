from django.urls import reverse
from rest_framework import status
from ninjadjangoapp.models import Task
from ninjadjangoapp.tests.base import BaseTestCase


class DeleteTaskByIdTestCase(BaseTestCase):

    def setUp(self):

        super().setUp()

        self.task = Task.objects.create(
            title="Sample Task",
            description="This is a sample task",
            status="pending",
            due_date="2024-12-31"
        )

        self.valid_url = reverse(self.get_test_path('delete_task_by_id'), kwargs={'id': self.task.id})
        self.invalid_url = reverse(self.get_test_path('delete_task_by_id'), kwargs={'id': 9999})


    def test_delete_task_by_id_success(self):
        """
        測試成功根據 id 刪除任務
        """

        response = self.client.delete(self.valid_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 確認任務已被刪除
        response_check = self.client.get(self.valid_url)
        self.assertEqual(response_check.status_code, status.HTTP_400_BAD_REQUEST)



    def test_delete_task_by_id_wrong_id(self):
        """
        測試刪除不存在的任務 id
        """

        response = self.client.delete(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

