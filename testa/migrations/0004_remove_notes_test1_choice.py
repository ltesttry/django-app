# Generated by Django 5.0.2 on 2024-03-02 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testa', '0003_delete_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='test1',
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testa.question')),
            ],
        ),
    ]
