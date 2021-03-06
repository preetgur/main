# Generated by Django 2.2 on 2020-04-10 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.New_Blog')),
            ],
        ),
    ]
