# Generated by Django 4.1.2 on 2022-10-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_docs_user_alter_records_docs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='allegries',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='records',
            name='condition',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='records',
            name='history',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='records',
            name='labresults',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='records',
            name='notes',
            field=models.CharField(max_length=300),
        ),
    ]
