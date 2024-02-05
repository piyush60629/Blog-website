# Generated by Django 5.0.1 on 2024-02-02 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0014_blog_comment_blog_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_comment',
            old_name='comment',
            new_name='u_comment',
        ),
        migrations.RemoveField(
            model_name='blog_comment',
            name='blog_cat',
        ),
        migrations.AddField(
            model_name='blog_comment',
            name='blog_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myblogs.blog_post'),
            preserve_default=False,
        ),
    ]