# Generated by Django 2.2.6 on 2019-10-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100)),
                ('audience', models.IntegerField()),
                ('open_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
                ('watch_grade', models.CharField(max_length=100)),
                ('score', models.FloatField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
