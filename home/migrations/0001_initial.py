# Generated by Django 3.1.3 on 2022-01-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField()),
                ('name', models.CharField(max_length=5)),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
