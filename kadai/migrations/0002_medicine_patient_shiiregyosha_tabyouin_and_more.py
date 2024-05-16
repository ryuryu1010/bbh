# Generated by Django 5.0.6 on 2024-05-16 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadai', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicineid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('medicinename', models.CharField(max_length=64)),
                ('unit', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('patfname', models.CharField(max_length=64)),
                ('patiname', models.CharField(max_length=64)),
                ('hokenmei', models.CharField(max_length=64)),
                ('hokenexp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Shiiregyosha',
            fields=[
                ('shiireid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('shiiremei', models.CharField(max_length=64)),
                ('shiireaddress', models.CharField(max_length=64)),
                ('shiiretel', models.CharField(max_length=13)),
                ('shihonkin', models.IntegerField()),
                ('nouki', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tabyouin',
            fields=[
                ('tabyouinid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('tabyouinmei', models.CharField(max_length=64)),
                ('abyouinaddress', models.CharField(max_length=64)),
                ('tabyouintel', models.CharField(max_length=13)),
                ('byouinshihonk', models.IntegerField()),
                ('kyukyu', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emplname',
            new_name='empiname',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emppasswd',
            field=models.CharField(max_length=64),
        ),
    ]
