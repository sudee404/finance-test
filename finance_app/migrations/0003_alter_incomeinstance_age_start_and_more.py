# Generated by Django 4.0.4 on 2022-08-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0002_alter_incomeinstance_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeinstance',
            name='age_start',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='incomeinstance',
            name='age_stop',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='incomeinstance',
            name='growth',
            field=models.IntegerField(null=True),
        ),
    ]
