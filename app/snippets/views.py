from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    # 이상황에서 우리는 front로 우리의 데이터베이스로부터 select에서 보내주는 역할을 한다.
    if request.method == 'GET':
        # snippet 데이터 모두 불러옴 (model 전부 잡은거)
        snippets = Snippet.objects.all()
        # SnippetSerializer 이용해서 model을 python datatype으로 변환
        serializer = SnippetSerializer(snippets, many=True)
        # JsonResponse 이용해서 python datatype -> json type으로 변환
        return JsonResponse(serializer.data, safe=False)

    # 이 상황에서 우리는 front로부터 데이터를 받는 통로로 쓰인다.
    elif request.method == 'POST':
        # JSONParser를 이용해 request 날라온 data를 python data type으로 바꿈
        data = JSONParser().parse(request)
        # SnippetSerializer python data type -> Form
        serializer = SnippetSerializer(data=data)
        # serializer(ModelSerializer)이용해서 valid 유용성 거사
        if serializer.is_valid():
            serializer.save()
            # python datatype을 jsonResponse로 보내준다고?
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)