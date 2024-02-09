from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from celery.result import AsyncResult
from .tasks import my_task

@api_view(['POST'])
def taskDispatcher(request):
    task_id = 123 # generate a random id
    task=my_task.delay()  # Start the task asynchronously
    return Response({'task_id': task.id},status=status.HTTP_200_OK)

def show_page(request):
    return render(request, 'progbar.html')

def check_progress(request, task_id):
    """
    View to check the progress of a Celery task.
    """
    # Get the task result using the task ID
    result = AsyncResult(task_id)
    if result.state == 'PENDING':
        # Task is still pending, return progress 0%
        return JsonResponse({'progress': 0})

    elif result.state == 'SUCCESS':
        # Task is complete, return progress 100%
        return JsonResponse({'progress': 100})

    elif result.state == 'PROGRESS':
        # Task is in progress, get progress from result
        progress = result.info.get('progress', 0)
        return JsonResponse({'progress': progress})

    else:
        # Task failed or in an unexpected state, return an error
        return JsonResponse({'error': 'Task failed or in an unexpected state'})
