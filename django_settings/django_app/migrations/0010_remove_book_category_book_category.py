from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0009_bookcategory_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="category",
        ),
        migrations.AddField(
            model_name="book",
            name="category",
            field=models.ManyToManyField(
                blank=True, to="django_app.bookcategory", verbose_name="Тип"
            ),
        ),
    ]