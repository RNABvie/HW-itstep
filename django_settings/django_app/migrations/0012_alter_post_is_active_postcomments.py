from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("django_app", "0011_post_remove_book_category_delete_cities_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Активность поста"),
        ),
        migrations.CreateModel(
            name="PostComments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.TextField(default="", verbose_name="Текст комментария"),
                ),
                (
                    "date_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата и время создания",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        max_length=200,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        max_length=200,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_app.post",
                        verbose_name="К какому посту",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий к посту",
                "verbose_name_plural": "Комментарии к постам",
                "ordering": ("-date_time", "post"),
            },
        ),
    ]