# Generated by Django 4.2.5 on 2023-09-24 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_taskmodel_student_alter_taskmodel_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.studentmodel'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='subjects',
            field=models.ManyToManyField(related_name='tasks', to='api.subjectmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='subjectmodel',
            unique_together={('name', 'description')},
        ),
    ]
