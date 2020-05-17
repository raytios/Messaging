# Generated by Django 3.0.6 on 2020-05-12 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborate_Messaging_A00',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTimeStamp', models.DateTimeField(auto_created=True, auto_now=True)),
                ('messageType', models.CharField(choices=[('PST', 'Post'), ('RPLY', 'Reply')], db_column='Message_Type', default='PST', max_length=10)),
                ('message', models.TextField()),
                ('parentPostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Collaborate_Messaging_A00')),
            ],
        ),
    ]