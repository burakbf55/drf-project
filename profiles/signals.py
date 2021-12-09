from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile, ProfileDetail


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(
        instance.username,
        "__Created: ",
        created,  # -> Yeni profil olustugunda terminalde bool cikti alacagiz.
    )
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_first_detail_message(sender, instance, created, **kwargs):
    if created:
        ProfileDetail.objects.create(
            user_profile=instance,
            detail_message=f"{instance.user.username} klübe katıldı.",  # -> artık user.username yapısından bin kere bahsetmişizdir. Bu yapı user değişkenindeki username'i alıyor.
        )
