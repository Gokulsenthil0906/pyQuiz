# Generated by Django 4.0.1 on 2022-03-11 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_alter_resultmaths_maths_easy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultchemistry',
            name='chemistry_easy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resultchemistry',
            name='chemistry_hard',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resultchemistry',
            name='chemistry_medium',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resultphysics',
            name='physics_easy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resultphysics',
            name='physics_hard',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resultphysics',
            name='physics_medium',
            field=models.IntegerField(default=0),
        ),
    ]