# Generated by Django 5.0.1 on 2024-02-02 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0017_blog_comments_delete_blog_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog_comments',
            new_name='blog_comment',
        ),
    ]
