from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import apis

app_name = 'restaurant'
urlpatterns = [
    # as_view 안붙혀서 데이터 안떴나??
    # as_view class 에 만들어지는 get, post를 사용해서 request를 사용할 수 있는 함수들을 만들어 준다.
    path('restaurants/', apis.RestaurantListCreateAPIView.as_view()),
    path('restaurants/<int:pk>/', apis.RestaurantRetrieveUpdateDestroyAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
