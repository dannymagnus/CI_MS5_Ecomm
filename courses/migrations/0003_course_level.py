# Generated by Django 3.2 on 2022-06-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'General Enquiry'), ('4', 'Professional')], default='1', max_length=2),
        ),
    ]
