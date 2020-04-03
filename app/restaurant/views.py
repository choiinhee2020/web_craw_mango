from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.models import Restaurant
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

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
# @csrf_exempt
# def restaurant_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Restaurant.objects.all()
#         serializer = RestaurantSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
