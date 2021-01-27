# Generated by Django 2.2 on 2021-01-23 16:30

from django.db import migrations, models
import django.db.models.deletion
import jietu.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doamin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='域名')),
                ('status', models.CharField(default=False, max_length=5, verbose_name='是否截图')),
            ],
            options={
                'verbose_name': '域名',
                'verbose_name_plural': '域名',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='DoaminExpirationDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateField(unique=True, verbose_name='域名过期时间')),
            ],
            options={
                'verbose_name': '域名过期时间',
                'verbose_name_plural': '域名过期时间',
            },
        ),
        migrations.CreateModel(
            name='DoaminType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domaintype', models.CharField(blank=True, max_length=32, null=True, verbose_name='域名类型')),
            ],
            options={
                'verbose_name': '域名类型',
                'verbose_name_plural': '域名类型',
                'ordering': ['-domaintype'],
            },
        ),
        migrations.CreateModel(
            name='Jietu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=jietu.models.jietu_directory_path, verbose_name='域名图片')),
                ('views', models.IntegerField(default=0, verbose_name='阅览量')),
                ('content', models.TextField(blank=True, null=True, verbose_name='网站内容')),
                ('domain', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jietu.Doamin', verbose_name='域名')),
            ],
            options={
                'verbose_name': '域名截图',
                'verbose_name_plural': '域名截图',
            },
        ),
        migrations.AddField(
            model_name='doamin',
            name='domaintype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jietu.DoaminType', verbose_name='域名类型'),
        ),
        migrations.AddField(
            model_name='doamin',
            name='expiration_date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jietu.DoaminExpirationDate', verbose_name='域名过期时间'),
        ),
    ]
