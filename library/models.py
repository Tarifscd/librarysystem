from django.db import models
from datetime import datetime



class AuthorManager(models.Manager):
    def data_create(self, data):
        return self.create(**data)

    def data_update(self, data_id, data):
        return self.filter(id=data_id).update(**data)

    def get_data(self, data):
        data_list = Author.objects.prefetch_related('book_set').all()
        if 'name' in data:
            data_list = data_list.filter(name=data['name'])

        return data_list



class BookManager(models.Manager):
    def data_create(self, data):
        return self.create(**data)

    def data_update(self, data_id, data):
        return self.filter(id=data_id).update(**data)

    def get_data(self, data):
        data_list = Book.objects.select_related('author').all()
        if 'author_name' in data:
            data_list = data_list.filter(author__name=data['author_name'])
        if 'genre' in data:
            data_list = data_list.filter(genre=data['genre'])
        if 'start_date' and 'end_date' in data:
            data_list = data_list.filter(published_date__range=[data['start_date'], data['end_date']])

        return data_list


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorManager()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

    def __str__(self):
        return self.title
