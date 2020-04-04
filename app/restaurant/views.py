# from django.http import Http404
# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from restaurant.models import Restaurant, RestaurantCategory
# from restaurant.serializers import RestaurantSerializer
#
#
# class RestaurantList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#
#     # list (나중에 drf-filter 사용하자!
#     def get(self, request, format=None):
#         restaurants = Restaurant.objects.all()
#         serializer = RestaurantSerializer(restaurants, many=True)
#         return Response(serializer.data)
#
#     # create / update
#     def post(self, request, format=None):
#         serializer = RestaurantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # def perform_create(self, serializer):
#     #     pass
#     #     serializer.save(owner=self.request.user)
#
#
# class RestaurantDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     # name_address1_unique (category + name + address1)
#     def get_object(self, pk):
#         try:
#             return Restaurant.objects.get(pk=pk)
#         except Restaurant.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = RestaurantSerializer(snippet)
#         return Response(serializer.data)
#     # patch??
#     # html form 에서는 get 과 post만 가능하다
#     # 이러한 메소드는 각각 언어마다 가지고 있는 http 통신 라이브러리를 이용해서 이렇게 보낼거야 할 수 있다.
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         # update 할 때 code도 필요한가?
#         # 유효성 검사를 serializer 가 가진  requirements를 다 검사한다
#         # partial = True create 할때 필수적인 요소들은 안넣어줘도 값이 바뀐다.
#         serializer = RestaurantSerializer(snippet, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         # 돌려 줄 데이터가 없기 때문에 HttpResponse를 보내준다
#         # sataus 204 는 성공은 했지만 보내줄 데이터가 없다는 뜻이다.
#         return Response(status=status.HTTP_204_NO_CONTENT)

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