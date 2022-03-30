# Generated by Django 4.0.3 on 2022-03-29 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='mod',
            name='mod_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mods.game'),
        ),
    ]