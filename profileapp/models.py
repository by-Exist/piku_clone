from django.db import models

from accountapp.models import CustomUser


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="유저")
    avatar = models.ImageField("아바타", upload_to="profile/%Y/%m/%d", blank=True)
    message = models.CharField("소개글", max_length=300, blank=True)