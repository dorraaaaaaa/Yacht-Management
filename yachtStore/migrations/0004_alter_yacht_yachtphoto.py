# Generated by Django 4.2.7 on 2023-12-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yachtStore', '0003_yacht_yid_alter_yacht_yachtphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yacht',
            name='yachtPhoto',
            field=models.ImageField(upload_to='photos/%y/%m/%d'),
        ),
    ]
