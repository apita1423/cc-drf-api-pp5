from rest_framework import generics, permissions, filters
from drf_api_pp5.permissions import IsOwnerOrReadOnly
from .models import Chronicle
from .serializers import ChronicleSerializer


class ChronicleList(generics.ListCreateAPIView):
    serializer_class = ChronicleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Chronicle.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'owner__username',
        'title',
        'category',
        'author',
    ]


class ChronicleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve news, update, or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChronicleSerializer
    queryset = Chronicle.objects.all()
