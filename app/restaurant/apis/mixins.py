# generic으로 바로 넘어가라!!!!


from rest_framework import generics, mixins

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantListCreateAPIView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RestaurantRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                            mixins.UpdateModelMixin,
                                            mixins.DestroyModelMixin,
                                            generics.GenericAPIView):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)