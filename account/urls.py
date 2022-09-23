from django.urls import path
## define here urls http//127.0.0.1:8000/

from .views import *

urlpatterns = [
    path('',signup_view , name='signup'),
    path('login/',login_view,name='login'),
    path("logout/", logout_view, name="logout"),
    path('store/',library_view,name='store'),
    path("outstock/", library_OutStock, name="outstock"),
    path('addbook/',addBook,name='addbook'),
    path('update/<int:bid>/',update_book,name='update'),
    path("delete/<int:bid>/", deleteBook, name="delete"),
    path('listout/<int:bid>/',BookListOut,name='listout'),
]
