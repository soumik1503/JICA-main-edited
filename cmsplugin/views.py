from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('file')
        if not image_file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        filename = f"uploads/{uuid.uuid4()}_{image_file.name}"
        saved_path = default_storage.save(filename, ContentFile(image_file.read()))
        file_url = default_storage.url(saved_path)

        return JsonResponse({'location': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)
