from django.urls import path
from .views import *

urlpatterns = [
    path('author/create/', AuthorCreateView.as_view(), name='home'),
    path('author/update/', AuthorUpdateView.as_view(), name='home'),
    path('author/get_data/<int:data_id>/', AuthorGetListView.as_view(), name='home'),
    path('author/delete/<int:data_id>/', AuthorDeleteView.as_view(), name='home'),

    path('book/create/', BookCreateView.as_view(), name='home'),
    path('book/update/', BookUpdateView.as_view(), name='home'),
    path('book/get_data/<int:data_id>/', BookGetListView.as_view(), name='home'),
    path('book/delete/<int:data_id>/', BookDeleteView.as_view(), name='home'),
]