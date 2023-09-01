from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0007_find"),
    ]

    operations = [
        migrations.CreateModel(
            name="IceCreamType",
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
                ("name", models.CharField(max_length=200, verbose_name="Название")),
            ],
        ),
        migrations.AlterField(
            model_name="find",
            name="tracks",
            field=models.ManyToManyField(
                blank=True, null=True, to="django_app.item", verbose_name="Трек код"
            ),
        ),
        migrations.CreateModel(
            name="IceCream",
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
                ("name", models.CharField(max_length=200, verbose_name="Название")),
                (
                    "ice_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_app.icecreamtype",
                        verbose_name="Тип",
                    ),
                ),
            ],
        ),
    ]