# Generated by Django 2.0.1 on 2019-07-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20190724_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_pass',
            field=models.BooleanField(default=False, verbose_name='Passed student'),
        ),
    ]
