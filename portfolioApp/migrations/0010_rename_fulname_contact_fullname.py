# Generated by Django 4.1.1 on 2022-11-28 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolioApp", "0009_rename_username_contact_fulname"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact", old_name="fulname", new_name="fullname",
        ),
    ]