from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),

    # Nested comments route
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
