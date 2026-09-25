from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        # --- Portfolio: models.py has resume + profile_photo, 0001 didn't ---
        migrations.AddField(
            model_name='portfolio',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),

        # --- Project: models.py has project_image, 0001 didn't ---
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),

        # --- Certification: models.py has these 5 extra fields, 0001 didn't ---
        migrations.AddField(
            model_name='certification',
            name='category',
            field=models.CharField(blank=True, max_length=150, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certification',
            name='cert_image',
            field=models.ImageField(blank=True, null=True, upload_to='certs/'),
        ),
        migrations.AddField(
            model_name='certification',
            name='cert_file',
            field=models.FileField(blank=True, null=True, upload_to='certs/'),
        ),
        migrations.AddField(
            model_name='certification',
            name='cert_url',
            field=models.URLField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certification',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),

        # --- Experience: models.py replaced the old free-text `duration`
        # field with start_date / end_date / is_current, but 0001 still
        # only has `duration`. Add the new columns and drop the old one. ---
        migrations.AddField(
            model_name='experience',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='experience',
            name='duration',
        ),
    ]
