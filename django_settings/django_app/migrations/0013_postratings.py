from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("django_app", "0012_alter_post_is_active_postcomments"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostRatings",
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
                ("status", models.BooleanField(default=False)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_app.post",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рейтинг к новости",
                "verbose_name_plural": "Рейтинги к новостям",
                "ordering": ("-post", "author"),
            },
        ),
    ]