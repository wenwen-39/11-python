# Generated by Django 3.1.5 on 2021-01-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20210107_0147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='people',
            new_name='injured',
        ),
        migrations.AddField(
            model_name='company',
            name='die',
            field=models.CharField(default='M', max_length=1000),
        ),
    ]
