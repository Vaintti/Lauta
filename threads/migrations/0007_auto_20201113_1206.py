# Generated by Django 3.1.3 on 2020-11-13 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0006_auto_20201113_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7d552f42-c784-4ef2-91fc-c145510975c1'), editable=False),
        ),
    ]
