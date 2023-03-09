# Generated by Django 4.1.7 on 2023-02-22 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('subject', models.CharField(max_length=250, verbose_name='subject')),
                ('to_email', models.TextField(max_length=250, verbose_name='To Email')),
                ('from_email', models.CharField(max_length=250, verbose_name='From Email')),
                ('html_body', models.TextField(verbose_name='HTML Body')),
                ('txt_body', models.TextField(blank=True, null=True, verbose_name='TXT Body')),
                ('completed', models.BooleanField(default=False, verbose_name='completed')),
                ('sent_count', models.IntegerField(default=0, verbose_name='Sent count')),
                ('failed_count', models.IntegerField(default=0, verbose_name='Failed count')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('token', models.CharField(max_length=32, verbose_name='Verification token')),
                ('verified', models.BooleanField(default=False, verbose_name='Verified?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'nets_core_verification_code',
            },
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Name')),
                ('html_body', models.TextField(help_text='You can use Django template language see: https://docs.djangoproject.com/en/4.1/ref/templates/language/ ', verbose_name='HTML BODY')),
                ('text_body', models.TextField(help_text='You can use Django template language see: https://docs.djangoproject.com/en/4.1/ref/templates/language/ ', verbose_name='TXT BODY')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled?')),
                ('use_for', models.CharField(choices=[('verification_code', 'Verification code: send each time a code is generated'), ('other', 'Other: Nets core not implemented use. You can use this from any view quering from nets_core.models.EmailTemplate')], default='other', max_length=50, verbose_name='Use template for')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250, verbose_name='subject')),
                ('to', models.TextField(max_length=250, verbose_name='To Email')),
                ('from_email', models.CharField(max_length=250, verbose_name='From Email')),
                ('body', models.TextField(verbose_name='HTML Body')),
                ('txt_body', models.TextField(blank=True, null=True, verbose_name='TXT Body')),
                ('sent', models.BooleanField(default=False, verbose_name='sent')),
                ('tries', models.IntegerField(default=0, verbose_name='tries')),
                ('sent_at', models.DateTimeField(null=True, verbose_name='Sent at')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='created')),
                ('custom_email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nets_core.customemail')),
            ],
        ),
    ]
