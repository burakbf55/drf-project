from profiles.api.permissions import DetailOwnerOrReadOnly, ProfileOwnerOrReadOnly
from profiles.api.serializers import (
    ProfileDetailSerializer,
    ProfileFotoSerializer,
    ProfileSerializer,
)
from profiles.models import Profile, ProfileDetail
from rest_framework import generics, mixins, permissions
from rest_framework.decorators import permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class ProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ProfileOwnerOrReadOnly]
    filter_backends = (SearchFilter,)  # birden fazla arama filtresi dahil edilebilir
    search_fields = ("city",)


class ProfileDetailViewSet(ModelViewSet):
    queryset = ProfileDetail.objects.all()
    serializer_class = ProfileDetailSerializer
    permissions_classes = [IsAuthenticated, DetailOwnerOrReadOnly]

    def get_queryset(self):
        queryset = ProfileDetail.objects.all()
        username = self.request.query_params.get(
            "username"
        )  # url'imizde belirleyecegimiz username parametresi

        if username:
            queryset = queryset.filter(user_profile__user__username=username)

        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


class ProfilFotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileFotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile

        return profile_object
