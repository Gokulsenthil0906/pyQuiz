# Generated by Django 4.0.1 on 2022-03-09 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='MathsEasy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.maths')),
            ],
        ),
        migrations.CreateModel(
            name='MathsHard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.maths')),
            ],
        ),
        migrations.CreateModel(
            name='MathsMedium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.maths')),
            ],
        ),
        migrations.CreateModel(
            name='Physics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsEasy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.physics')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsHard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.physics')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsMedium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.physics')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsMediumOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.physicsmedium')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsHardOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.physicshard')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsEasyOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.physicseasy')),
            ],
        ),
        migrations.CreateModel(
            name='MathsMediumOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.mathsmedium')),
            ],
        ),
        migrations.CreateModel(
            name='MathsHardOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.mathshard')),
            ],
        ),
        migrations.CreateModel(
            name='MathsEasyOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.mathseasy')),
            ],
        ),
    ]
