from django.conf.urls import *
from django.urls import path
from django.urls.conf import include
from profiles.api.views import (ProfileDetailViewSet, ProfileViewSet,
                                ProfilFotoUpdateView)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiller", ProfileViewSet)
router.register(r"durum", ProfileDetailViewSet, basename="durum")
from .views import SocialLoginView

urlpatterns = [
    path("", include(router.urls)),
    path("profil_foto/", ProfilFotoUpdateView.as_view(), name="profil_foto"),
    path('oauth/login/', SocialLoginView.as_view())
 ]
