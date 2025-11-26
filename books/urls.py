from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    BookListApiView,
    BookDetailApiView,
    BookDetailCustomApiView,
    BookDeleteApiView,
    BookUpdateApiView,
    BookCreateApiView,
    BookListCreateView,
    BookUpdateDeleteView,
    BookCustomCreateApiView,
    BookViewset,
)

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
    path('books/', BookListApiView.as_view(), name='book-list'),
    path('booklistcreate/', BookListCreateView.as_view(), name='book-list-create'),
    path('bookupdatedelete/<int:pk>/', BookUpdateDeleteView.as_view(), name='book-update-delete'),
    path('books/create/', BookCustomCreateApiView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailApiView.as_view(), name='book-detail'),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view(), name='book-delete'),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view(), name='book-update'),
]

urlpatterns = urlpatterns + router.urls
