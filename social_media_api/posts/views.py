from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, filters
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from notifications.utils import create_notification 


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])
        create_notification(
            recipient=Post.author,
            actor=self.request.user,
            verb="commented on your post",
            target=Post
        )


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class LikePostView(generics.GenericAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = self.get_object()

        if Like.objects.filter(post=post, user=request.user).exists():
            return Response({"error": "You already liked this post."}, status=400)

        Like.objects.create(post=post, user=request.user)
        create_notification(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

        return Response({"message": "Post liked successfully."}, status=200)


class UnlikePostView(generics.GenericAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = self.get_object()

        like = Like.objects.filter(post=post, user=request.user).first()
        if not like:
            return Response({"error": "You haven't liked this post."}, status=400)

        like.delete()
        return Response({"message": "Post unliked successfully."}, status=200)
