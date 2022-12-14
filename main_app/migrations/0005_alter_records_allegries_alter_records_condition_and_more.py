# Generated by Django 4.1.2 on 2022-10-17 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_records_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='allegries',
            field=models.CharField(default='none', max_length=150),
        ),
        migrations.AlterField(
            model_name='records',
            name='condition',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='records',
            name='docs',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='main_app.docs'),
        ),
        migrations.AlterField(
            model_name='records',
            name='history',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='records',
            name='labresults',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='records',
            name='notes',
            field=models.CharField(default='none', max_length=300),
        ),
    ]
