# Generated by Django 4.2.1 on 2023-06-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatallotment',
            name='Institue_name',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AddField(
            model_name='seatallotment',
            name='closing_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seatallotment',
            name='gender',
            field=models.CharField(default='Neutral', max_length=100),
        ),
        migrations.AddField(
            model_name='seatallotment',
            name='opening_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seatallotment',
            name='round_no',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='seatallotment',
            name='year',
            field=models.IntegerField(default=2022),
        ),
        migrations.AlterField(
            model_name='seatallotment',
            name='branch',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='seatallotment',
            name='category',
            field=models.CharField(default='Open', max_length=100),
        ),
    ]
