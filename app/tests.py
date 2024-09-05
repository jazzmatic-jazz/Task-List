from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskTests(TestCase):
    '''
        Basic Test Case for checking
        - filter by status
        - sort by priority
        - sort by due date
        - filter + sorting
    '''
    def setUp(self):
        '''
            Creating dummy test task objects in db
        '''
        Task.objects.create(title="Task 1", status="todo", priority="1", due_date="2024-09-10")
        Task.objects.create(title="Task 2", status="in_progress", priority="2", due_date="2024-09-12")
        Task.objects.create(title="Task 3", status="done", priority="3", due_date="2024-09-08")
        Task.objects.create(title="Task 4", status="todo", priority="2", due_date="2024-09-15")

    def test_filter_by_status(self):
        '''
            test case for filtering by status
            - todo
            - in_progress
            - done
        '''
        response = self.client.post(reverse('task_list'), {'status': 'todo'})
        self.assertEqual(response.status_code, 200)
        tasks = response.context['tasks']
        self.assertEqual(tasks.count(), 2)
        self.assertTemplateUsed(response, 'app/task_list.html')

    def test_sort_by_priority(self):
        '''
            test case for sorting by priority
            - high(3)
            - medium(2)
            - low(1)
        '''
        response = self.client.post(reverse('task_list'), {'sort_by': 'priority'})
        self.assertEqual(response.status_code, 200)
        tasks = response.context['tasks']
        self.assertEqual(tasks.count(), 4)
        self.assertEqual([task.priority for task in tasks], ['1', '2', '2', '3'])

    def test_sort_by_due_date(self):
        '''
            test case for sorting by due dates
        '''
        response = self.client.post(reverse('task_list'), {'sort_by': 'due_date'})
        self.assertEqual(response.status_code, 200)
        tasks = response.context['tasks']
        self.assertEqual(tasks.count(), 4)
        self.assertEqual([task.due_date.strftime('%Y-%m-%d') for task in tasks], ['2024-09-08', '2024-09-10', '2024-09-12', '2024-09-15'])

    def test_filter_and_sort(self):
        '''
            test case for filtering + sorting combination
        '''
        response = self.client.post(reverse('task_list'), {'status': 'todo', 'sort_by': 'priority'})
        self.assertEqual(response.status_code, 200)
        tasks = response.context['tasks']
        self.assertEqual(tasks.count(), 2)
        self.assertEqual([task.priority for task in tasks], ['1', '2'])
