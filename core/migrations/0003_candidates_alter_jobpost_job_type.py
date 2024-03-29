# Generated by Django 4.1.3 on 2022-11-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_jobpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('degree', models.CharField(choices=[('bachelor', 'Bachelor'), ('master', 'Master'), ('doctor', 'Doctorant'), ('noedu', 'No education')], max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('full_time', 'Full time'), ('part_time', 'Part time'), ('freelance', 'Freelance'), ('internship', 'Internship'), ('termporary', 'Termporary')], max_length=100),
        ),
    ]
