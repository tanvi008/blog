# Generated by Django 4.0.2 on 2023-01-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blog_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
