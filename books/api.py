from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def get_user_credentials(request):
    if request.method == 'GET':
        users = User.objects.all()

        credentials = []

        for user in users:
            credentials.append({
                'login': user.username,
                'password': user.password,
                'role': user.first_name,
            })

        return JsonResponse({'credentials': credentials})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
