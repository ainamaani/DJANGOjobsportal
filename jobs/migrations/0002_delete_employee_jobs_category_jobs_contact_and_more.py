# Generated by Django 4.2.1 on 2023-05-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='jobs',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='contact',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='experience',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='jobtype',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='location',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='qualifications',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='salary',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='skills',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='company',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='email',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
