# Generated by Django 4.1.1 on 2022-11-28 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolioApp", "0006_alter_blog_blog_contents"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="blog_header",),
    ]