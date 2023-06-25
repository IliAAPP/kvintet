import json
from django.views.decorators.csrf import csrf_exempt
from store.models import Data
from django.views.decorators.http import require_POST


def index(request):
    return render(request, "index.html")


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import django

django.setup()

from django.core.exceptions import ObjectDoesNotExist


@require_POST
@csrf_exempt
def save_data(request):
    request_body = json.loads(request.body)
    id = request_body['id']
    collected = request_body['collected']
    add_file = request_body['add_file']
    finish_button_pressed = request_body['finish_button_pressed']

    if id and collected and add_file and finish_button_pressed:
        try:
            data = Data.objects.get(id=id)
            data.delete()
        except ObjectDoesNotExist:
            pass

        return JsonResponse({'message': 'Data deleted successfully.'})

    if id and collected and add_file:
        data = Data(id=id, collected=collected, add_file=add_file)
        data.save()

        return JsonResponse({'message': 'Data saved successfully.'})

    return JsonResponse({'message': 'Invalid or incomplete data provided.'})


from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import TaskToAuthor


def task_to_author(request):
    if request.method == 'POST':
        author_id = request.POST.get('author_id')

        deadline_date = request.POST.get('deadline_date')

        progress = request.POST.get('progress')

        task = TaskToAuthor(author_id=author_id, deadline_date=deadline_date, progress=progress)

        task.save()

        # Возвращаем ответ в формате JSON
        response_data = {
            'status': 'success',
            'message': 'Task created successfully.'
        }
        return JsonResponse(response_data)

    # Если метод запроса не POST, то просто возвращаем пустой JSON-ответ
    response_data = {
        'status': 'error',
        'message': 'Invalid request method.'
    }
    return JsonResponse(response_data)
