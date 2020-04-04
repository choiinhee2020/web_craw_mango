from django.urls import path, include

from snippets.views import SnippetList, SnippetDetail, UserDetail, UserList
app_name='snippets'
urlpatterns = [
    path('snippets/', SnippetList),
    path('snippets/<int:pk>/', SnippetDetail),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),

]