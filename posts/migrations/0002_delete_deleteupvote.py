# Generated by Django 3.2 on 2021-04-21 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DeleteUpvote",
        ),
    ]
