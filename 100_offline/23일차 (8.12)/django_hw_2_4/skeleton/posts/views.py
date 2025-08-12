from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def posts_get_or_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

@api_view(['PUT', 'DELETE'])
def posts_update_or_delete(request, posts_pk):
    posts = Post.objects.get(pk=posts_pk)
    if request.method == 'PUT':
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        posts.delete()
        return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)