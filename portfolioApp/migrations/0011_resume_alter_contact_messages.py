# Generated by Django 4.1.1 on 2022-11-29 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolioApp", "0010_rename_fulname_contact_fullname"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resume",
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
                ("education", models.CharField(default="", max_length=50)),
                ("educ_date", models.CharField(default="2018-2022", max_length=15)),
                ("edu_description", models.TextField(blank=True, null=True)),
                ("experience", models.CharField(default="", max_length=50)),
                ("exp_year", models.CharField(default="2018-2022", max_length=20)),
                ("exp_description", models.TextField(blank=True, null=True)),
                ("skills_name", models.CharField(default="", max_length=50)),
                ("skills_perc", models.IntegerField()),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="contact", name="messages", field=models.TextField(default=""),
        ),
    ]
