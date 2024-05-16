from rest_framework import generics, permissions, filters
from drf_api_pp5.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'owner__username',
        'title',
        'city',
        'country',
        'price',
        'date',
    ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event, update, or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
