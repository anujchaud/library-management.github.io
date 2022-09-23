from django.contrib import admin
from .models import Book, User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =['book_name','book_author']