from django.urls import path, include
from .views import BookList, BookViewSet, CustomAuthToken
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# newRouter = DefaultRouter()
# newRouter.register(r'login', MyAPIView, basename='login')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)), # All routes registered with router
    path('token/', CustomAuthToken.as_view(), name='api_token'),
]