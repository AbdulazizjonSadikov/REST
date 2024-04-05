from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSeriaLizer
from rest_framework import generics, status
# Create your views here.

# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSeriaLizer


class BookListApiView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer_data = BookSeriaLizer(books, many=True).data
        data = {
            'status' : f"Returned {len(books)} books",
            'books' : serializer_data
        }



# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSeriaLizer
    
    
class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSeriaLizer(book).data
            data = {
                'status' : 'Succesfull',
                'book' : serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                     {'status':'does not exits',
                 'message':'Book is not found'},
                status=status.HTTP_404_NOT_FOUND
            )

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSeriaLizer


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status':True,
                'message':"Succesfully deleted"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status':False,
                'Message':"Book is not found"
            }, status=status.HTTP_404_BAD_REQUEST)
    

# class BookUpdateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSeriaLizer


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSeriaLizer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                'status':True,
                'message':f"Book {book_saved} updated succesfully"
                
            
            }
        )
    
class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSeriaLizer
    
# class BookListCreateApiView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSeriaLizer
    
    
    
class BookListCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSeriaLizer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f"book save database",
                'books':data
            }
            return Response(data)
        
        
class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSeriaLizer
    
    
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSeriaLizer(books, many=True)
    return Response(serializer.data)


