# Generated by Django 4.2.5 on 2023-09-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daynumber',
            options={'ordering': ('created_at', 'updated_at'), 'verbose_name': 'Kun nomi', 'verbose_name_plural': 'Kun'},
        ),
        migrations.AlterField(
            model_name='daynumber',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt'),
        ),
        migrations.AlterField(
            model_name='daynumber',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='daynumber',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqt'),
        ),
        migrations.AlterField(
            model_name='daynumber',
            name='view_home',
            field=models.BooleanField(default=False, verbose_name='Faollik'),
        ),
    ]