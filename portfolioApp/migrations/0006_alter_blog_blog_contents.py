# Generated by Django 4.1.1 on 2022-11-28 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolioApp", "0005_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blog_contents",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
