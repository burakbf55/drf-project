from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    foto = models.ImageField(null=True, blank=True, upload_to="profil_fotolari/%Y/%m/")

    def __str__(self):
        return (
            self.user.username
        )  # --> Profile class'ında oluşturduğumuz user değişkeninin username'ini al demektir.

    class Meta:
        verbose_name_plural = "Profiles"

    def save(
        self, *args, **kwargs
    ):  # --> Fotoğrafımızı görüntülerken eğer fotoğraf boyutu çok büyükse o fotoğrafı kısıtladık(belirli bir boyuta soktuk.)
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.foto.path)


class ProfileDetail(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    detail_message = models.CharField(max_length=240)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profile Messages"

    def __str__(self):
        return str(self.user_profile)
