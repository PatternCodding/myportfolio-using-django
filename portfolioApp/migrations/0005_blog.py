# Generated by Django 4.1.1 on 2022-11-28 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolioApp", "0004_navbar_remove_about_navbar"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("blog_header", models.CharField(default="", max_length=10)),
                ("blog_img", models.ImageField(upload_to="blogs_img")),
                ("blog_date", models.DateTimeField(auto_now_add=True)),
                ("blog_description", models.CharField(max_length=50)),
                ("blog_contents", models.TextField(default="")),
            ],
        ),
    ]
