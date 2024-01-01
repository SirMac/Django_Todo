# Generated by Django 5.0 on 2024-01-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=50)),
                ('createdat', models.DateTimeField(verbose_name='Created At')),
            ],
        ),
    ]