from django.db import models
from django.contrib import admin
class Library(models.Model):
    serial_no=models.IntegerField(primary_key=True);
    book_name=models.CharField(max_length=40);
    author_name=models.CharField(max_length=20);
    publisher=models.CharField(max_length=30);
    dateofpub=models.DateField();
class LibraryAdmin(admin.ModelAdmin):
    list_display=("serial_no","book_name","author_name","publisher","dateofpub");
