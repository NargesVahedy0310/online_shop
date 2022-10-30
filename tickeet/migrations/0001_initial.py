# Generated by Django 4.1.2 on 2022-10-29 21:16

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
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('open', 'باز'), ('close', 'بسته')], default=('open', 'باز'), max_length=10)),
                ('department', models.CharField(choices=[('teacher', 'معلم'), ('money', 'مالی')], default=('teacher', 'معلم'), max_length=10)),
                ('products', models.CharField(choices=[('mobile', 'مبایل'), ('laptap', 'لپ تاپ')], default=('mobile', 'مبایل'), max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MessageTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, upload_to='File')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickeet.ticket')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]