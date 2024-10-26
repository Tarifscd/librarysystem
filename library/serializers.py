from rest_framework import serializers

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    date_of_birth = serializers.DateField(required=False)


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    author_id = serializers.CharField(read_only=True)
    genre = serializers.CharField(max_length=15, required=False)
    published_date = serializers.DateField(required=False)