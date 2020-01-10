# Generated by Django 3.0.2 on 2020-01-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200110_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='member',
            field=models.ManyToManyField(to='blog.TeamMember'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
