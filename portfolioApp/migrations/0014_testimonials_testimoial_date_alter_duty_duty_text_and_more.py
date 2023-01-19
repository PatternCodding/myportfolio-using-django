# Generated by Django 4.1.1 on 2022-11-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "portfolioApp",
            "0013_client_duty_testimonials_remove_about_client_header_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="testimonials",
            name="testimoial_date",
            field=models.CharField(default="Y-M-D", max_length=50),
        ),
        migrations.AlterField(
            model_name="duty", name="duty_text", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="testimonials",
            name="testimoial_name",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]