# Generated by Django 3.0.7 on 2020-06-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200628_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='default-user.png', upload_to='user_pics/'),
        ),
    ]
