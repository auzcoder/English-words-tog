# Generated by Django 4.2.5 on 2023-09-16 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0006_wordlevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='words.wordlevel'),
        ),
    ]
