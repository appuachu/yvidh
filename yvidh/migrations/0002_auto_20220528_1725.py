# Generated by Django 3.2.7 on 2022-05-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yvidh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='description_event',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_coordinator',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='month_event',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='register_link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='caption_gallery',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shows',
            name='description_show',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shows',
            name='show_name',
            field=models.TextField(),
        ),
    ]
