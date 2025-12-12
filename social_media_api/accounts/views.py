# from rest_framework import status, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth import authenticate, get_user_model
# from .serializers import UserRegistrationSerializer, UserLoginSerializer
# from rest_framework.authtoken.models import Token
# from django.shortcuts import get_object_or_404

# User = get_user_model()

# # Create your views here.

# # Registration View
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Login View (Token Authentication)
# class LoginView(APIView):
#     def post(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# # User Profile View (Authenticated users only)
# class ProfileView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         return Response({
#             'username': user.username,
#             'bio': user.bio,
#             'profile_picture': user.profile_picture.url if user.profile_picture else None,
#             'followers': [follower.username for follower in user.followers.all()]
#         })

# class FollowUserView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, user_id):
#         target_user = get_object_or_404(User, id=user_id)

#         if target_user == request.user:
#             return Response({"error": "You cannot follow yourself."}, status=400)

#         request.user.following.add(target_user)
#         return Response({"message": f"You are now following {target_user.username}."})


# class UnfollowUserView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, user_id):
#         target_user = get_object_or_404(User, id=user_id)

#         if target_user == request.user:
#             return Response({"error": "You cannot unfollow yourself."}, status=400)

#         request.user.following.remove(target_user)
#         return Response({"message": f"You unfollowed {target_user.username}."})


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        if target_user == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target_user)

        return Response(
            {"message": f"You are now following {target_user.username}."},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        if target_user == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target_user)

        return Response(
            {"message": f"You unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )
