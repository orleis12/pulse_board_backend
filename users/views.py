from rest_framework import viewsets
from .models import User, LandingPage, UserActivity
from .serializer import UserSerializer, LandingPageSerializer, UserActivitySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  
    
class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer
    permission_classes = [IsAuthenticated] 

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [IsAuthenticated] 
    
class CreateMultipleUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        users_data = request.data.get('users', [])

        if not users_data or len(users_data) == 0:
            return Response({"error": "Debes enviar un array de objetos users"}, status=status.HTTP_400_BAD_REQUEST)

        created_users = []
        for user_data in users_data:
            try:
                user_data['password'] = make_password(user_data['password']) 
                serializer = UserSerializer(data=user_data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                created_users.append(serializer.data['username'])
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"created_users": created_users}, status=status.HTTP_201_CREATED)

class CreateMultipleUsersWithActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        users_data = request.data.get('users', [])

        if not users_data or len(users_data) == 0:
            return Response({"error": "Debes enviar un array de objetos users"}, status=status.HTTP_400_BAD_REQUEST)

        created_users = []
        created_activities = []
        for user_data in users_data:
            try:
                
                user_data['password'] = make_password(user_data['password']) 
                user_serializer = UserSerializer(data=user_data)
                user_serializer.is_valid(raise_exception=True)
                user = user_serializer.save()  
                

                activity_data = {
                    'user': user.id,
                    'login_time': user_data.get('login_time', '2024-11-07T20:58:12.775523Z'),
                    'session_duration': user_data.get('session_duration', '00:00:00'),
                    'clicked_button_1': user_data.get('clicked_button_1', 0),
                    'clicked_button_2': user_data.get('clicked_button_2', 0)
                }
                activity_serializer = UserActivitySerializer(data=activity_data)
                activity_serializer.is_valid(raise_exception=True)
                activity_serializer.save()  

                
                created_users.append(user.username)
                created_activities.append(activity_serializer.data)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "created_users": created_users,
            "created_activities": created_activities
        }, status=status.HTTP_201_CREATED)
    
    
class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        
        
        return Response({
            'id':user.id,
            'token': token.key,
            'is_superuser': user.is_superuser,  
            'username': user.username,
            'email': user.email
        }, status=status.HTTP_200_OK)
    