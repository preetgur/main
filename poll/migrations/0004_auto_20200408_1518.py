# Generated by Django 2.2 on 2020-04-08 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='answer',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
