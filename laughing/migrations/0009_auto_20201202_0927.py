# Generated by Django 2.2 on 2020-12-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laughing', '0008_auto_20201202_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postq',
            name='category',
            field=models.CharField(choices=[('A', 'Agriculture'), ('B', 'Banking'), ('E', 'Electrical'), ('EC', 'Economics'), ('M', 'Mechanic'), ('S', 'Science')], max_length=2),
        ),
    ]
