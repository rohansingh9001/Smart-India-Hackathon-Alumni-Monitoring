# Generated by Django 3.0.2 on 2020-01-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniDetailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('About', models.CharField(max_length=200)),
                ('Work', models.CharField(max_length=50)),
                ('Year_Joined', models.IntegerField()),
                ('status', models.CharField(default=False, max_length=10)),
            ],
        ),
    ]
