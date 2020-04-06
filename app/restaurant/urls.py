from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .apis import generics, viewsets



app_name = 'restaurant'

router = DefaultRouter()
router.register(r'restaurants', viewsets.RestaurantViewSet)

urlpatterns_viewset = [
    path('restaurants/', viewsets.RestaurantViewSet.as_view({
        'get':'list',
        'post':'create',
    })),
    path('restaurants/<int:pk>/', viewsets.RestaurantViewSet.as_view({
        'get':'retrieve',
        'post':'partial_update',
        'delete':'destroy',
    })),
    # path('restaurants/<int:pk>',viewsets.RestaurantViewSet.as_view)
]

urlpatterns_api_view = [
    # as_view 안붙혀서 데이터 안떴나??
    # as_view class 에 만들어지는 get, post를 사용해서 request를 사용할 수 있는 함수들을 만들어 준다.
    # include() 함수를 사용해서 아래와 같이 api-view접두어를 붙이도록 설정
    # 별도의 urlpatterns를 갖고 있을 리스트 뱐수 필요

    # localhost:8000/api-view/restaurants/
    path('restaurants/', generics.RestaurantListCreateAPIView.as_view()),
    # localhost:8000/api-view/restaurants/1/
    path('restaurants/<int:pk>/', generics.RestaurantRetrieveUpdateDestroyAPIView.as_view()),
]


urlpatterns = {
    path('api-view/', include(urlpatterns_api_view)),
    path('viewset/', include(urlpatterns_viewset)),
    # path('router/', include(router.urls)),

}

urlpatterns = format_suffix_patterns(urlpatterns)
