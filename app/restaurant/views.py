from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.models import Restaurant, RestaurantCategory
from restaurant.serializers import RestaurantSerializer


class RestaurantList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    # list (나중에 drf-filter 사용하자!
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    # create / update
    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     pass
    #     serializer.save(owner=self.request.user)


class RestaurantDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # name_address1_unique (category + name + address1)
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RestaurantSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RestaurantSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class RestaurantCategoryList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#
#     # list (나중에 drf-filter 사용하자!
#     def get(self, request, format=None):
#         restaurants_category = RestaurantCategory.objects.all()
#         serializer = RestaurantSerializer(restaurants_category, many=True)
#         return Response(serializer.data)
#
#     # create / update
#     def post(self, request, format=None):
#         serializer = RestaurantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)