# Generated by Django 4.0.4 on 2022-08-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0003_alter_incomeinstance_age_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeinstance',
            name='age_start',
            field=models.PositiveIntegerField(blank=True, default=40),
        ),
        migrations.AlterField(
            model_name='incomeinstance',
            name='age_stop',
            field=models.PositiveIntegerField(blank=True, default=90),
        ),
        migrations.AlterField(
            model_name='incomeinstance',
            name='description',
            field=models.CharField(default='Others', max_length=200),
        ),
        migrations.AlterField(
            model_name='incomeinstance',
            name='growth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
