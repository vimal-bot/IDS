# Generated by Django 2.2.4 on 2020-12-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0018_auto_20201204_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(default='default.jpg', upload_to='profile')),
                ('post', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='history',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
