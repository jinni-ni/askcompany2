from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from .models import Post

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs,many=True)
#         return Response(serializer.data)
#
# public_post_list = PublicPostListAPIView.as_view()
#
# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs,many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # 인증이 되어 있음을 보장 받을 수 있음
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message']
    #odering_fields
    #ordering

    def perform_create(self, serializer):
        # FIXME : 인증이 되어있다는 가정 하에, author 지정
        author = self.request.user # User or AnonymousUser
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)


    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)

        #serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



    # def list(self, request, *args, **kwargs):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body :", request.body) # 운영시 logger 를 추천
    #     print("request.POST :", request.POST)
    #
    #     return super().dispatch(request, *args, **kwargs)

# # Create your views here.
# def post_list(request):
#     # 2개 분기
#     pass
#
# def post_detail(request):
#     # 3개 분기
#     pass

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instagram/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post' : PostSerializer(post).data,
        })
