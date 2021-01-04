from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nickname = models.CharField(
        "닉네임",
        unique=True,
        max_length=12,
        validators=[MinLengthValidator(4, "네글자 이상 입력해주세요.")],
    )