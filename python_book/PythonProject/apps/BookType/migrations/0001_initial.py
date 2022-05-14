# Generated by Django 2.2.5 on 2019-09-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('bookTypeId', models.AutoField(primary_key=True, serialize=False, verbose_name='图书类型id')),
                ('bookTypeName', models.CharField(default='', max_length=40, verbose_name='图书类型名称')),
                ('days', models.IntegerField(default=0, verbose_name='可借阅天数')),
            ],
            options={
                'verbose_name': '图书类别',
                'verbose_name_plural': '图书类别',
                'db_table': 't_BookType',
            },
        ),
    ]
