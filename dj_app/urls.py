from django.contrib import admin
from django.urls import path
from store.views import index
from .tasks import get_tasks
from store.views import save_data, task_to_author
from .api import get_user_credentials

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name="index"),
    path('api/user-credentials/', get_user_credentials, name='user_credentials'),
    path('api/tasks/', get_tasks, name='get_tasks'),
    path('api/save_data/', save_data, name='save_data'),
    path('api/tasks/task_to_author/', task_to_author, name='task_to_author')
]

# http://127.0.0.1:8000/api/tasks/
# http://127.0.0.1:8000/api/user-credentials/
# http://127.0.0.1:8000/api/save_data/
# http://127.0.0.1:8000/api/tasks/task_to_author/ ---
