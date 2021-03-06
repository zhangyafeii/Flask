# Generated by Django 2.0.5 on 2018-10-05 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20181005_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p', to='rbac.Menu')),
            ],
        ),
        migrations.AlterModelOptions(
            name='permissiontoaction',
            options={'verbose_name_plural': '权限表'},
        ),
        migrations.AlterModelOptions(
            name='roletopremissiontoaction',
            options={'verbose_name_plural': '角色分配权限'},
        ),
    ]
