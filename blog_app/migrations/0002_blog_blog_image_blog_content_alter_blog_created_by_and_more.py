# Generated by Django 4.1.4 on 2022-12-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(default='', upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_by',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]