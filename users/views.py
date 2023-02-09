from .models import User, UserDetail
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework import viewsets
from rest_framework.pagination import CursorPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "id"
    # pagination_class = CursorPagination


# class UserViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         snippets = get_object_or_404(User, id=pk)
#         serializer = UserSerializer(snippets)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         user = get_object_or_404(User, id=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
