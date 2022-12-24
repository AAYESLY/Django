from django.http import HttpResponse
from django.shortcuts import render, redirect
from firstapp import models

# Create your views here.
from django.urls import reverse


def hello(request):
    return HttpResponse("Hello, this is your first app!")


def login(request):
    return HttpResponse(reverse("app01:login"))


def add_book(request):
    book = models.Book(title="ldfgaxdT", price=570, publish="XD家属区", pub_date="2022-12-12")
    book.save()
    return HttpResponse("<p>书籍 {{ book.title }} 数据添加成功! </p>")


def select_book(request):
    books = models.Book.objects.filter(price__range=[0, 110]).order_by('-price')

    # print(books[0]['title'], books[0]['price'])
    return HttpResponse(books)
        # HttpResponse("<p> 查找成功 </p>")



