# tasks/tests.py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ayush', password='secret123')
        # login to obtain token
        res = self.client.post('/api/auth/login/', {'username': 'ayush', 'password': 'secret123'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.access = res.data['access']
        self.auth = {'HTTP_AUTHORIZATION': f'Bearer {self.access}'}

    def test_create_and_list_tasks(self):
        payload = {'title': 'Test Task', 'description': 'desc', 'completed': False}
        res = self.client.post('/api/tasks/', payload, format='json', **self.auth)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        res = self.client.get('/api/tasks/', **self.auth)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['title'], 'Test Task')

    def test_retrieve_update_delete(self):
        task = Task.objects.create(owner=self.user, title='T1')
        # retrieve
        res = self.client.get(f'/api/tasks/{task.id}/', **self.auth)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # update
        res = self.client.put(f'/api/tasks/{task.id}/', {'title':'T1-upd','completed':True}, format='json', **self.auth)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(res.data['completed'])

        # delete
        res = self.client.delete(f'/api/tasks/{task.id}/', **self.auth)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_cannot_access_others_tasks(self):
        other = User.objects.create_user(username='other', password='pass12345')
        other_task = Task.objects.create(owner=other, title='secret')

        res = self.client.get(f'/api/tasks/{other_task.id}/', **self.auth)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)  # not your task

        res = self.client.put(f'/api/tasks/{other_task.id}/', {'title':'hack'}, format='json', **self.auth)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
