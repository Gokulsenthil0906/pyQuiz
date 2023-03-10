# Generated by Django 4.0.1 on 2022-03-10 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0006_delete_resultchemistry_delete_resultmaths_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultPhysics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physics_hard', models.IntegerField()),
                ('physics_easy', models.IntegerField()),
                ('physics_medium', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultMaths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maths_hard', models.IntegerField()),
                ('maths_easy', models.IntegerField()),
                ('maths_medium', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultChemistry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemistry_hard', models.IntegerField()),
                ('chemistry_easy', models.IntegerField()),
                ('chemistry_medium', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
