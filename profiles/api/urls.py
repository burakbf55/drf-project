from django.urls import path
from django.urls.conf import include
from profiles.api.views import (
    ProfileDetailViewSet,
    ProfileViewSet,
    ProfilFotoUpdateView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiller", ProfileViewSet)
router.register(r"durum", ProfileDetailViewSet, basename="durum")


urlpatterns = [
    path("", include(router.urls)),
    path("profil_foto/", ProfilFotoUpdateView.as_view(), name="profil_foto"),
]
