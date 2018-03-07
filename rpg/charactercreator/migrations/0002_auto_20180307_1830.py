# Generated by Django 2.0.3 on 2018-03-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0001_initial'),
        ('charactercreator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleric',
            name='inventory',
            field=models.ManyToManyField(to='armory.Items', verbose_name='Items the character has'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='inventory',
            field=models.ManyToManyField(to='armory.Items', verbose_name='Items the character has'),
        ),
        migrations.AddField(
            model_name='mage',
            name='inventory',
            field=models.ManyToManyField(to='armory.Items', verbose_name='Items the character has'),
        ),
        migrations.AddField(
            model_name='thief',
            name='inventory',
            field=models.ManyToManyField(to='armory.Items', verbose_name='Items the character has'),
        ),
        migrations.AlterField(
            model_name='cleric',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Character's name"),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Character's name"),
        ),
        migrations.AlterField(
            model_name='mage',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Character's name"),
        ),
        migrations.AlterField(
            model_name='thief',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Character's name"),
        ),
    ]
