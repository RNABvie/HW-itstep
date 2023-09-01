from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0002_alter_product_options_product_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Complaint",
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
                    "username",
                    models.CharField(max_length=300, verbose_name="Наименование"),
                ),
                ("text", models.TextField(max_length=3000, verbose_name="Описание")),
                ("type", models.CharField(max_length=300, verbose_name="Наименование")),
                ("is_active", models.BooleanField(default=True)),
                ("date_time", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name": "Жалоба",
                "verbose_name_plural": "Жалобы",
                "ordering": ("-is_active", "date_time", "type"),
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to="images/products",
                verbose_name="Изображение",
            ),
        ),
    ]