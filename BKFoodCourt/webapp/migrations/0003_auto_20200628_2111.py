# Generated by Django 3.0.7 on 2020-06-28 14:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200625_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_ready',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
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
    ]
