# Generated by Django 4.1.2 on 2022-10-30 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickeet', '0003_alter_messageticket_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageticket',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickeet.ticket'),
        ),
    ]