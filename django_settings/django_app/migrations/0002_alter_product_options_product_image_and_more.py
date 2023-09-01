from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("-is_active", "title"),
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                default=None,
                null=True,
                upload_to="images/products",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(max_length=3000, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=300, verbose_name="Наименование"),
        ),
    ]