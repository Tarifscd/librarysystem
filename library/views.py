from django.forms import model_to_dict
from rest_framework.permissions import IsAuthenticated, AllowAny
# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from library.models import Book
from library.serializers import BookSerializer

from library.models import Author
from library.serializers import AuthorSerializer


class AuthorCreateView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # Handle POST requests
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Data not valid!", "data": request.data}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = serializer.data
        print('serializer_data ================== ', serializer_data)

        try:
            Author.objects.data_create(serializer_data)
            return Response({"message": "Data created sucessfully.", "data": serializer_data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            pass

        return Response({"message": "Data not created!", "data": serializer_data}, status=status.HTTP_400_BAD_REQUEST)


class AuthorUpdateView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # Handle POST requests
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Data not valid!", "data": {}}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = serializer.data
        print('serializer_data ================== ', serializer_data)

        author_id = request.data['author_id']

        try:
            Book.objects.data_update(author_id, serializer_data)
            return Response({"message": "Data updated sucessfully.", "data": serializer_data}, status=status.HTTP_200_OK)

        except Exception as e:
            pass

        return Response({"message": "Data not updated!", "data": serializer_data}, status=status.HTTP_400_BAD_REQUEST)


class AuthorGetListView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # Handle POST requests
    def post(self, request):
        try:
            data = Author.objects.get_data(request.data)
            data = model_to_dict(data)
            return Response({"message": "Data retrieved sucessfully.", "data": data}, status=status.HTTP_200_OK)

        except Exception as e:
            pass

        return Response({"message": "Data not retrieved!", "data": {}}, status=status.HTTP_400_BAD_REQUEST)


class AuthorDeleteView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # Handle POST requests
    def get(self, request, data_id):
        try:
            data = Author.objects.delete(id=data_id)
            return Response({"message": "Data retrieved sucessfully.", "data": {"data_d": data_id}}, status=status.HTTP_200_OK)

        except Exception as e:
            pass

        return Response({"message": "Data not retrieved!", "data": {"data_d": data_id}}, status=status.HTTP_400_BAD_REQUEST)


class BookCreateView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # Handle POST requests
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Data not valid!", "data": {}}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = serializer.data
        print('serializer_data ================== ', serializer_data)
        author_obj = Author.objects.filter(id=serializer_data['author_id']).last()
        serializer_data.pop('author_id')
        serializer_data['author'] = author_obj

        try:
            Book.objects.data_create(serializer_data)
            return Response({"message": "Data created sucessfully.", "data": serializer_data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            pass

        return Response({"message": "Data not created!", "data": serializer_data}, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # Handle POST requests
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Data not valid!", "data": {}}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = serializer.data
        print('serializer_data ================== ', serializer_data)

        book_id = request.data['book_id']
        author_obj = Author.objects.filter(id=serializer_data['author_id']).last()
        serializer_data.pop('author_id')
        serializer_data['author'] = author_obj

        try:
            Book.objects.data_update(book_id, serializer_data)
            return Response({"message": "Data updated sucessfully.", "data": serializer_data}, status=status.HTTP_200_OK)

        except Exception as e:
            pass

        return Response({"message": "Data not updated!", "data": serializer_data}, status=status.HTTP_400_BAD_REQUEST)


class BookGetListView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # Handle POST requests
    def post(self, request, data_id):
        try:
            data = Book.objects.get_data(request.data)
            data = model_to_dict(data)
            return Response({"message": "Data retrieved sucessfully.", "data": data}, status=status.HTTP_200_OK)

        except Exception as e:
            pass

        return Response({"message": "Data not retrieved!", "data": {}}, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # Handle POST requests
    def get(self, request, data_id):
        try:
            data = Book.objects.delete(id=data_id)
            return Response({"message": "Data retrieved sucessfully.", "data": {"data_d": data_id}}, status=status.HTTP_200_OK)

        except Exception as e:
            pass

        return Response({"message": "Data not retrieved!", "data": {"data_d": data_id}}, status=status.HTTP_400_BAD_REQUEST)