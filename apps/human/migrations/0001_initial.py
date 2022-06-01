# Generated by Django 4.0.4 on 2022-06-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=250, unique=True, verbose_name='과제 번호')),
                ('title', models.CharField(max_length=500, verbose_name='과제명')),
                ('department', models.CharField(blank=True, max_length=250, verbose_name='진료과')),
                ('institute', models.CharField(blank=True, max_length=250, verbose_name='연구 책임 기관')),
                ('target', models.CharField(blank=True, max_length=250, verbose_name='전체 목표 연구 대상자 수')),
                ('duration', models.CharField(blank=True, max_length=250, verbose_name='연구 기간')),
                ('type', models.CharField(blank=True, max_length=250, verbose_name='연구 종류')),
                ('stage', models.CharField(blank=True, max_length=250, verbose_name='임상 시험 단계')),
                ('scope', models.CharField(blank=True, max_length=250, verbose_name='연구 범위')),
            ],
            options={
                'db_table': 'research',
            },
        ),
    ]