# Generated by Django 2.2.4 on 2020-06-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Yazar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=30)),
                ('soyisim', models.CharField(max_length=30)),
                ('kitaplar', models.ManyToManyField(to='app1.Kitap')),
            ],
        ),
    ]
