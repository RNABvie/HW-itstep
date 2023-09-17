from django.contrib.auth.models import User
import random

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class UserProfile(models.Model):
    """
    Модель, которая содержит расширение для стандартной модели пользователя веб-платформы
    """

    user = models.OneToOneField(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Модель пользователя",
        help_text='<small class="text-muted">Тут лежит "ссылка" на модель пользователя</small><hr><br>',
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",  # user.profile
    )
    avatar = models.ImageField(verbose_name="Аватарка", upload_to="static/media/users", default=None, null=True, blank=True)

    class Meta:
        """Вспомогательный класс"""

        app_label = "auth"
        ordering = ("-user", "avatar")
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return f"<UserProfile {self.user.username}>"



@receiver(post_save, sender=User)
def create_user_model(sender, instance, created, **kwargs):
    UserProfile.objects.get_or_create(user=instance)
    # created - за булево значение, "создана ли модель"
    # if created:
    #     UserProfile.objects.get_or_create(user=instance)




class UserAuthToken(models.Model):
    user = models.ForeignKey(verbose_name="Пользователь", to=User, on_delete=models.CASCADE)
    token = models.CharField(verbose_name="Токен", max_length=300)
    # можно добавить время создания и не пускать позже 3 дней
    # можно добавить одноразовое использование
    # ...

    class Meta:
        app_label = "django_app"
        ordering = ("-user", "token")
        verbose_name = "Токен доступа"
        verbose_name_plural = "Токены доступа"

    def __str__(self):
        return f"{self.user.username} {self.token}"

    @staticmethod
    def token_generator() -> str:
        def generate_track(length: int, characters: str) -> str:
            return "".join(random.choice(characters) for _ in range(length))

        f1 = "NL"
        f2 = generate_track(4, "1234567890")
        f3 = generate_track(4, "1234567890")
        f4 = generate_track(3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # f1  f2   f3   f4
        # NL13541342KJG
        return f"{f1}{f2}{f3}{f4}"