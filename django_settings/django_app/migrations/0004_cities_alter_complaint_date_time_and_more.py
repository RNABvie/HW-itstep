from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0003_complaint_alter_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cities",
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
                ("name", models.CharField(max_length=300, verbose_name="Наименование")),
                (
                    "index",
                    models.CharField(
                        max_length=300, unique=True, verbose_name="Индекс города"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        max_length=300, verbose_name="Тип отделения(сортировка/приём)"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активность"),
                ),
            ],
            options={
                "verbose_name": "Отделение",
                "verbose_name_plural": "Отделения",
                "ordering": ("-is_active", "type", "name"),
            },
        ),
        migrations.AlterField(
            model_name="complaint",
            name="date_time",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата и время подачи"
            ),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Активность"),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="type",
            field=models.CharField(max_length=300, verbose_name="Тип жалобы"),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="username",
            field=models.CharField(max_length=300, verbose_name="Имя пользователя"),
        ),
    ]