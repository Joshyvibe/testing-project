# createsuperuser.py

from django.contrib.auth.models import User
from django.core.management import call_command
from django.http import JsonResponse

def create_superuser(request):
    # Check if the request is authorized
    # Implement your authentication logic here

    # Call the createsuperuser management command
    call_command('createsuperuser', username='admin', email='admin@example.com', password='admin', interactive=False)

    # Check if the superuser has been successfully created
    try:
        user = User.objects.get(username='admin')
        return JsonResponse({'message': 'Superuser created successfully', 'user': {'username': user.username, 'email': user.email}})
    except User.DoesNotExist:
        return JsonResponse({'message': 'Failed to create superuser'}, status=500)
