# Generated by Django 4.2.6 on 2023-11-08 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0002_breed_alter_dog_author_dog_breed_parent_breed'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dog', to='shelter.breed', verbose_name='порода'),
        ),
    ]
