# Generated by Django 3.1.4 on 2021-01-16 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='flights',
            name='destions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='airline.airport'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='airline.airport'),
        ),
    ]
