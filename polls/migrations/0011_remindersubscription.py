# Generated by Django 2.0.3 on 2018-11-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_feedbackdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('preferred_time', models.CharField(max_length=64)),
                ('token', models.CharField(max_length=128)),
            ],
        ),
    ]
