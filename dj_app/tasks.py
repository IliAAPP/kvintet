from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from store.models import Task


@csrf_exempt
def get_tasks(request):
    if request.method == 'GET':
        try:
            if Task.objects.exists():
                tasks = Task.objects.all()

                task_data = []

                for task in tasks:
                    task_data.append({
                        'name_task': task.name_task,
                        'field_size': task.field_size,
                        'max_deadlines': task.max_deadlines
                    })

                return JsonResponse({'tasks': task_data})
            else:
                return JsonResponse({'message': 'No tasks found'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

# @csrf_exempt
# def add_task(request):
#     if request.method == 'POST':
#         try:
#             name_task = request.POST.get('name_task')
#             field_size = request.POST.get('field_size')
#             max_deadlines = request.POST.get('max_deadlines')
#
#             task = Task(name_task=name_task, field_size=field_size, max_deadlines=max_deadlines)
#             task.save()
#
#             return JsonResponse({'message'})
