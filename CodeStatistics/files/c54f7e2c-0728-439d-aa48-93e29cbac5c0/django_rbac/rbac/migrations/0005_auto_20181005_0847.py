# Generated by Django 2.0.5 on 2018-10-05 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20181005_0840'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name_plural': '菜单表'},
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.Menu'),
        ),
    ]
