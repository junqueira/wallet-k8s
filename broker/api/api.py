from rest_framework import generics, permissions
# from .serializers import UserSerializer, PostSerializer, PhotoSerializer, RouteSerializer, MapSerializer
# from .models import User
# from django.contrib.auth.models import User

from .wallet_buy import Wallet
# from .permissions import PostAuthorCanEditPermission
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


# class UserList(generics.ListAPIView):
#     model = User
#     serializer_class = UserSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]
#
#
# class UserDetail(generics.RetrieveAPIView):
#     model = User
#     serializer_class = UserSerializer
#     lookup_field = 'username'


class WalletMixin(object):
    model = Wallet
    # serializer_class = WalletSerializer
    # permission_classes = [
    #     PostAuthorCanEditPermission
    # ]

    def pre_save(self, obj):
        """Force author to the current user on save"""
        obj.author = self.request.user
        return super(WalletMixin, self).pre_save(obj)


class WalletList(WalletMixin, generics.ListCreateAPIView):
    # pass
    # model = Post
    queryset = Wallet.objects.all()
    # serializer_class = WalletSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # permission_classes = (IsAdminUser,)

    # def get_queryset(self):
    #     queryset = super(PostList, self).get_queryset()
    #     return queryset.filter(author_id=self.kwargs.get('pk'))
    #

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_paginate_by(self):
        """
        Use smaller pagination for HTML representations.
        """
        if self.request.accepted_renderer.format == 'html':
            return 20
        return 100

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


# class WalletDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
#     pass
    # model = Post
    # serializer_class = PostSerializer
    # lookup_field = 'username'