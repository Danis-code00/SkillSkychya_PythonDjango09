from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate, login as auth_login 

@api_view(['GET'])
# Create your views here.
def first_view(request):
    return JsonResponse({"message": "Hello World"})

def welcome(request):
    return JsonResponse({"greetings": "Welcome to Django Class"})

@api_view(['GET'])
def second_view(request):
    return JsonResponse({"messages": "Hello World from second view"})

@api_view(['POST'])
@authentication_classes([])
@permission_classes([any])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    #Peform authentication login here
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return JsonResponse({'message': 'Login sucessful'})
    else:
        return JsonResponse({'message': 'Invalid credentials'}, status = 401)