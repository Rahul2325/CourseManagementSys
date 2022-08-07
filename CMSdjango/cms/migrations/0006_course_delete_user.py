# Generated by Django 4.0.4 on 2022-08-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_user_delete_userlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=50)),
                ('CourseCredits', models.CharField(max_length=2)),
                ('CourseImage', models.ImageField(upload_to='')),
                ('Desc', models.TextField()),
                ('Tags', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]