from django.views import View
from django.http import JsonResponse


class HealthCheck(View):
    def get(self, request):
        data = {
            'success': True,
            'method': str(request.method).lower(),
            'message': 'Alien API. Stay away.',
        }
        return JsonResponse(data, status=200)
