from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Posts
from .serializers import PostsListSerializer, PostsListSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_get_or_create(request):
    if request.method == 'GET':
        articles = Posts.objects.all()
        
        serializer = PostsListSerializer(articles, many=True)
        
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostsListSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)