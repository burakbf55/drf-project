from profiles.models import Profile, ProfileDetail
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True
    )  # StringRelatedField user verimizi integer yerine string gösterir -> Burak kullanıcısının id'si 1 ise stringrelatedfield
    # olmadan 1 diye geri dönüş alırız. StringRelatedField 1 diye aldığımız geri dönüşü 'Burak' yapar.
    foto = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = ['user','bio', 'city', 'foto']


class ProfileFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["foto"]  # ('foto',) şeklinde de gösterilir.


class ProfileDetailSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileDetail
        fields = ['user_profile', 'detail_message', 'created_time', 'updated_time']
