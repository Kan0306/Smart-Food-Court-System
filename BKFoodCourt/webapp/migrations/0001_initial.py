# Generated by Django 3.0.7 on 2020-07-01 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('description', models.TextField(blank=True, max_length=300)),
                ('price', models.DecimalField(decimal_places=0, max_digits=8)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stallname', models.CharField(max_length=500)),
                ('owner', models.CharField(blank=True, max_length=50)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ONGOING', 'Ongoing'), ('ACCEPT', 'Accept'), ('CONFIRMED', 'Confirmed'), ('WAITING', 'Waiting'), ('READY', 'Ready'), ('COMPLETED', 'Completed')], default='ONGOING', max_length=100)),
                ('order_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Order')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='belongs_to_stall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Menu'),
        ),
    ]
