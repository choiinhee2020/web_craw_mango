from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from restaurant import views

app_name = 'restaurant'
urlpatterns = [
    # as_view 안붙혀서 데이터 안떴나??
    path('restaurant/', views.RestaurantList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
