# Generated by Django 3.0.7 on 2020-07-02 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
        ('users', '0003_remove_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone', models.CharField(blank=True, max_length=500)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('own_stall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Menu')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]