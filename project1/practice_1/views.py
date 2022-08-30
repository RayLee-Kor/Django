from django.http import JsonResponse
from rest_framework.decorators import api_view
import jwt

# Create your views here.
def hello(request):
    return JsonResponse({"name" : "test"})

@api_view(['GET'])
def get_data(request):
    input_value = request.GET.get('input')
    return JsonResponse({"response":input_value})

@api_view(['POST'])
def post_data(request):
    input_value = request.data['input']
    return JsonResponse({"response":input_value})

def jwtfuc(request):
    token = jwt.encode(payload={},key='asdf123',algorithm='HS256').decode('utf-8')
    return JsonResponse({"jwt": token})