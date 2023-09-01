from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("django_app", "0010_remove_book_category_book_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                    "title",
                    models.CharField(max_length=300, verbose_name="Наименование"),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="images/products",
                        verbose_name="Изображение",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата и время подачи",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
                "ordering": ("-is_active", "title"),
            },
        ),
        migrations.RemoveField(
            model_name="book",
            name="category",
        ),
        migrations.DeleteModel(
            name="Cities",
        ),
        migrations.DeleteModel(
            name="Complaint",
        ),
        migrations.RemoveField(
            model_name="find",
            name="tracks",
        ),
        migrations.RemoveField(
            model_name="find",
            name="user",
        ),
        migrations.RemoveField(
            model_name="icecream",
            name="ice_type",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
        migrations.DeleteModel(
            name="Book",
        ),
        migrations.DeleteModel(
            name="BookCategory",
        ),
        migrations.DeleteModel(
            name="Find",
        ),
        migrations.DeleteModel(
            name="IceCream",
        ),
        migrations.DeleteModel(
            name="IceCreamType",
        ),
        migrations.DeleteModel(
            name="Item",
        ),
    ]