from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator


class WorldCup(models.Model):

    # TODO: 이미지 최소 갯수 제한하기. 2개?

    # TODO: 이미지 뿐만 아닌 다른 타입의 월드컵도 구현하기
    # MEDIA_TYPE_CHOICES = [
    #     ("I", "Image"),  # 이미지
    #     ("L", "Link"),  # 외부 동영상 링크
    #     ("T", "Text"),  # 텍스트
    # ]
    # media_type = models.CharField(
    #     "월드컵 타입", choices=MEDIA_TYPE_CHOICES, default="I"
    # )

    # TODO: 공개/비공개/비밀 구현하기

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(
        "타이틀", max_length=127, validators=[MinLengthValidator(10, "열 글자 이상 입력해주세요.")]
    )
    sub_title = models.CharField("부제", blank=True, max_length=255)
    thumbnail = models.ImageField("썸네일", upload_to="worldcup_thumbnail/%Y/%m/%d")
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    play_count = models.IntegerField("플레이 횟수", editable=False, default=0)


class Player(models.Model):

    world_cup = models.ForeignKey(
        WorldCup, verbose_name="월드컵", on_delete=models.CASCADE
    )

    title = models.CharField("제목", max_length=31)
    image = models.ImageField("이미지", upload_to="worldcup/%Y/%m/%d/%h")
    game_win_count = models.IntegerField("월드컵 승리 횟수", editable=False, default=0)
    o2o_win_count = models.IntegerField("1:1 승리 횟수", editable=False, default=0)