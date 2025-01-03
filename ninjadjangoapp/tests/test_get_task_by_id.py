from django.urls import reverse
from rest_framework import status
from ninjadjangoapp.models import Task
from ninjadjangoapp.tests.base import BaseTestCase



class GetTaskByIdTestCase(BaseTestCase):

    def setUp(self):
        
        super().setUp()

        self.task = Task.objects.create(
            id=1,
            title="Sample Task",
            description="This is a sample task",
            status="pending",
            due_date="2024-12-31"
        )

        self.valid_url = reverse(self.get_test_path('get_task_by_id'), kwargs={'id': self.task.id})
        self.invalid_url = reverse(self.get_test_path('get_task_by_id'), kwargs={'id': 9999}) 



    def test_get_task_by_id_success(self):
        """
        測試成功根據 id 查詢任務
        """

        response = self.client.get(self.valid_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task = response.json()['data']
        expected_fields = ['title', 'description', 'status', 'due_date']

        for field in expected_fields:
            self.assertEqual(
                task[field], 
                getattr(self.task, field),
                msg=f"task 內的 {field} 預期為 {getattr(self.task, field)}，實際為 {task[field]}"
            )



    def test_get_task_by_id_wrong_id(self):
        """
        測試查詢不存在的任務 id
        """

        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)