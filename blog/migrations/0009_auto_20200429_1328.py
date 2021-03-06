# Generated by Django 2.2 on 2020-04-29 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20200425_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.Comment'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='comment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dis_likes', to='blog.Comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.Comment'),
        ),
        migrations.CreateModel(
            name='User_Additional_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
