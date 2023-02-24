# Generated by Django 4.1.6 on 2023-02-23 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0006_rename_subscribe_authors_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='user',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]