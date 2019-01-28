from rest_framework.viewsets import ModelViewSet

# from django_filters.rest_framework import DjangoFilterBackend
from myblog.models import Post
from myblog.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = '__all__'
    # filter_backends = (DjangoFilterBackend,)
