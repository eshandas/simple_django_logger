# Generated by Django 2.0.3 on 2018-04-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_level', models.IntegerField(choices=[(1, 'ERROR'), (2, 'DEBUG'), (3, 'WARN'), (4, 'INFO')], default=4)),
                ('message', models.TextField(blank=True)),
                ('stack_trace', models.TextField(blank=True)),
                ('tag', models.CharField(blank=True, max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Event Log',
                'verbose_name_plural': 'Event Logs',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_level', models.IntegerField(choices=[(1, 'ERROR'), (2, 'DEBUG'), (3, 'WARN'), (4, 'INFO')], default=4)),
                ('request_url', models.CharField(blank=True, max_length=2083)),
                ('request_method', models.CharField(blank=True, max_length=10)),
                ('get_data', models.TextField(blank=True)),
                ('request_body', models.TextField(blank=True)),
                ('cookies', models.TextField(blank=True)),
                ('meta', models.TextField(blank=True)),
                ('exception_type', models.CharField(blank=True, max_length=2083)),
                ('message', models.TextField(blank=True)),
                ('stack_trace', models.TextField(blank=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('user_name', models.CharField(blank=True, max_length=255)),
                ('request_browser', models.CharField(blank=True, max_length=255)),
                ('request_os', models.CharField(blank=True, max_length=255)),
                ('request_device', models.CharField(blank=True, max_length=255)),
                ('response_body', models.TextField(blank=True)),
                ('response_status', models.CharField(blank=True, max_length=255)),
                ('response_headers', models.TextField(blank=True)),
                ('response_content_type', models.CharField(blank=True, max_length=255)),
                ('is_mobile', models.BooleanField(default=False)),
                ('is_tablet', models.BooleanField(default=False)),
                ('is_touch_capable', models.BooleanField(default=False)),
                ('is_pc', models.BooleanField(default=False)),
                ('is_bot', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(blank=True, max_length=10)),
                ('url', models.CharField(blank=True, max_length=2043)),
                ('request_data', models.TextField(blank=True)),
                ('request_headers', models.TextField(blank=True)),
                ('response_text', models.TextField(blank=True)),
                ('response_status', models.IntegerField(null=True)),
                ('response_reason', models.CharField(blank=True, max_length=255)),
                ('response_time', models.IntegerField(blank=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('user_name', models.CharField(blank=True, max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Request Log',
                'verbose_name_plural': 'Request Logs',
            },
        ),
    ]
