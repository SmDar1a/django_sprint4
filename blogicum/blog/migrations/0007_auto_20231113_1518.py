# Generated by Django 3.2.16 on 2023-11-13 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'default_related_name': 'comments', 'ordering': ('created_at',), 'verbose_name': 'комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'default_related_name': 'posts', 'ordering': ('-pub_date',), 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.location', verbose_name='Местоположение'),
        ),
    ]
