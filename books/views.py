from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from books.models import Book
from books.serializers import BookSerializer


# -----------------------
# LIST (APIView)
# -----------------------
class BookListApiView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        data = {
            "status": f"Returned {len(books)} books.",
            "books": serializer.data
        }
        return Response(data)


# -----------------------
# DETAIL (APIView)
# -----------------------
class BookDetailCustomApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        serializer = BookSerializer(book)
        data = {
            "status": "Successful",
            "book": serializer.data
        }
        return Response(data)


# -----------------------
# CRUD USING GENERICS
# -----------------------

class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteApiView(APIView):


    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                "status": "Successfully deleted",
                "message": "Book has been deleted"
            },)

        except Book.DoesNotExist:
            return Response({
                "status": "False",
                "message": "Book is not found"
            },)

class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book, id=pk)

        serializer = BookSerializer(instance=book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": f"Book '{book.title}' updated successfully",
                    "updated_data": serializer.data
                },

            )

        return Response(
            {
                "status": False,
                "errors": serializer.errors
            },

        )
class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# -----------------------
# CREATE USING APIView
# -----------------------
class BookCustomCreateApiView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "Book created",
                "book": serializer.data
            })
        return Response(serializer.errors, status=400)


# -----------------------
# LIST + CREATE
# -----------------------
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# -----------------------
# RETRIEVE + UPDATE + DELETE
# -----------------------
class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# -----------------------
# Function-based API
# -----------------------
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
