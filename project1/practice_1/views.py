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

# 로그인 구현 -> 토큰 받아오기
@api_view(['POST'])
def login(request):
    input_name = request.data['name']
    input_password = request.data['password']
    token = jwt.encode(payload={"name":input_name},key='asd123',algorithm='HS256').decode('utf-8')
    data = {"token" : token, "ID" : input_name}
    return JsonResponse({"data":data})
