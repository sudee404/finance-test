# Generated by Django 4.0.4 on 2022-08-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0007_alter_incomeinstance_age_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeinstance',
            name='growth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]