from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from .models import Book, Publisher
from first_app.serializer import BookSerializer, PublisherSerializer
from rest_framework.views import APIView

# Create your views here.
import first_app
from first_app.models import Book


def hello(request, name: str, num: int):
    return HttpResponse(f"{num}. {name.title()}, welcome to Django")


def index(request):
    context = [1, 2, 5]

    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua. "
    return render(request, "first_app/index.html", context={"obj": context,
                                                            "name": "Wale", "is_major": False, "text": text})


def redirect(request):
    print(reverse('first_app:about'))
    return HttpResponseRedirect(reverse('first_app:about'))


class BookList(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def about(request):
    return render(request, 'first_app/about.html')


class PublisherList(APIView):
    def get(self, request):
        queryset = Publisher.objects.all()
        serializer = PublisherSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class PublisherDetail(APIView):
    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    def delete(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        serializer = PublisherSerializer(publisher, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

