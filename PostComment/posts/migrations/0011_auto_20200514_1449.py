# Generated by Django 3.0.6 on 2020-05-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20200514_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='messageType',
            field=models.CharField(choices=[('POST', 'Post'), ('REPLY', 'Reply')], db_column='Message_Type', default=1, max_length=10),
        ),
    ]
