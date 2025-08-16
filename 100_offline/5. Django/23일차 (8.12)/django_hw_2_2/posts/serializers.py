from rest_framework import serializers
from .models import Posts

class PostsListSerializer(serializers.ModelSerializer):
    # 직렬화를 한다.
    class Meta:
        # 모델에 대한 정보를 토대로
        model = Posts
        fields = ('id', 'title',)
    
# 위에는 오로지 전체 목록만을 위한 시리얼라이저 였다면,
# 이번에는 범용적으로 게시글에 대한 전반적인 처리가 가능한 시리얼라이저
class PostsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'