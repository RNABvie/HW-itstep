from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0005_item_alter_cities_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="track",
            field=models.CharField(
                max_length=500, unique=True, verbose_name="Трек код"
            ),
        ),
    ]