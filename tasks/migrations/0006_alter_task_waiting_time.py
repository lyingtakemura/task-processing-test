# Generated by Django 4.2.3 on 2023-07-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='waiting_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]