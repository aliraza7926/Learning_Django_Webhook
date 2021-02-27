from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def test(request):
    body = request.body
    print(body)    
    return HttpResponse(status=200)
    
    