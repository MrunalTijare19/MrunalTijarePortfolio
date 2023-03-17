# Generated by Django 4.1.4 on 2023-03-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('desciption', models.TextField()),
                ('authname', models.CharField(max_length=15)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('timeStamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]