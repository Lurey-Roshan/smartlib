# Generated by Django 3.2.7 on 2021-09-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_pic',
            field=models.ImageField(default='image/pdf.png', upload_to='image/'),
        ),
    ]
