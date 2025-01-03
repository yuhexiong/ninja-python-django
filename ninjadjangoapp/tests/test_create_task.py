import json
from django.urls import reverse
from rest_framework import status
from ninjadjangoapp.tests.base import BaseTestCase



class CreateTaskTestCase(BaseTestCase):

    def setUp(self):

        super().setUp()

        self.valid_payload = {
            "title": "Test Task",
            "description": "This is a test task",
            "status": "Pending",
            "due_date": "2024-12-31"
        }
        self.invalid_payload = {
            "description": "Invalid task",
            "status": "Pending",
            "due_date": "2024-12-31"
        }

        self.url = reverse(self.get_test_path('create_task'))


    def test_create_task_success(self):
        """
        測試創建任務成功
        """

        response = self.client.post(
            self.url,
            data = json.dumps(self.valid_payload), 
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('data', response.json(), msg="response 內應該要有 'data'")
        self.assertIsInstance(response.json()['data'], object, msg="'response.data' 預期為 object 類型")

        task = response.json()['data']
        expected_fields = ['title', 'description', 'status', 'due_date']

        for field in expected_fields:
            self.assertEqual(
                task[field], 
                self.valid_payload[field],
                msg=f"task 內的 {field} 預期為 {self.valid_payload[field]}，實際為 {task[field]}"
            )



    def test_create_task_failure(self):
        """
        測試創建任務失敗
        """

        response = self.client.post(
            self.url,
            data = json.dumps(self.invalid_payload), 
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
