# Generated by Django 3.0.7 on 2020-06-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200628_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='default-user.png', upload_to='user_pics/'),
        ),
    ]