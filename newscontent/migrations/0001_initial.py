# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newscontent.models
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('title_eng', models.CharField(max_length=255, verbose_name=b'Adress')),
                ('latitude', models.CharField(max_length=31, null=True, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xbe\xd1\x82\xd0\xb0', blank=True)),
                ('longitude', models.CharField(max_length=31, null=True, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb0', blank=True)),
            ],
            options={
                'db_table': 'adress',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
                ('title_eng', models.CharField(max_length=255, verbose_name=b'City')),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.FileField(upload_to=newscontent.models.company_directory_logo_upload, blank=True)),
                ('company_name', models.CharField(unique=True, max_length=127, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8')),
                ('contact_person', models.CharField(max_length=63, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbb\xd0\xb8\xd1\x86\xd0\xbe')),
                ('contact_email', models.EmailField(max_length=254, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 email')),
                ('company_type', models.CharField(max_length=31, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8')),
                ('company_site', models.URLField(verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8')),
                ('keystone_person_in_charge', models.CharField(max_length=63, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbb\xd0\xb8\xd1\x86\xd0\xbe \xd0\xb8\xd0\xb7 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b Keystone')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0')),
                ('title_eng', models.CharField(max_length=255, verbose_name=b'Country')),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=31, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('surname', models.CharField(max_length=31, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('university', models.CharField(max_length=127, null=True, verbose_name=b'\xd0\x92\xd0\xa3\xd0\x97', blank=True)),
                ('speciality', models.CharField(max_length=127, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5\xd1\x82', blank=True)),
                ('grad_year', models.IntegerField(blank=True, max_length=4, null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xbe\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)])),
                ('linkedin', models.URLField(verbose_name=b'LinkedIn', blank=True)),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8f')),
                ('current_cv', models.FileField(blank=True, upload_to=newscontent.models.user_directory_cv_upload, verbose_name=b'Curriculum Vitae (CV)', validators=[newscontent.models.validate_file_extension])),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('user_class', models.CharField(default=b'E', max_length=1, verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f', choices=[(b'E', b'\xd0\x9e\xd0\xb1\xd1\x8b\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'), (b'S', b'\xd0\x90\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'), (b'C', b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')])),
                ('agree_terms', models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb3\xd0\xbb\xd0\xb0\xd1\x81\xd0\xb5\xd0\xbd \xd1\x81 \xd1\x83\xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb8\xd1\x8f\xd0\xbc\xd0\xb8 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x81\xd0\xbe\xd0\xb3\xd0\xbb\xd0\xb0\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('agree_hr', models.BooleanField(default=True, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb3\xd0\xbb\xd0\xb0\xd1\x81\xd0\xb5\xd0\xbd \xd0\xbd\xd0\xb0 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8f \xd0\xb4\xd0\xbb\xd1\x8f HR \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb9')),
                ('cheked_profile', models.BooleanField(default=False, verbose_name=b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8c')),
                ('company', models.ForeignKey(default=1, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', to='newscontent.Company')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'custom_user',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbc\xd0\xb5\xd1\x80\xd0\xbe\xd0\xbf\xd1\x80\xd0\xb8\xd1\x8f\xd1\x82\xd0\xb8\xd1\x8f')),
                ('title_eng', models.CharField(max_length=40, verbose_name=b'Event name')),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description_eng', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('date', models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0')),
                ('timezone', models.CharField(max_length=31, null=True, verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd0\xbf\xd0\xbe\xd1\x8f\xd1\x81', blank=True)),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('adress', models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True, to='newscontent.Adress')),
                ('city', models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', blank=True, to='newscontent.City', null=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='EventClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choose_type', models.CharField(max_length=31, verbose_name=b'\xd0\x9e\xd0\xb4\xd0\xbd\xd0\xb0 \xd0\xb2\xd1\x81\xd1\x82\xd1\x80\xd0\xb5\xd1\x87\xd0\xb0 \xd0\xb8\xd0\xbb\xd0\xb8 \xd0\xba\xd1\x83\xd1\x80\xd1\x81')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'db_table': 'eventclass',
            },
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=31, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('lname', models.CharField(max_length=31, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('permit', models.BooleanField(verbose_name=b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd1\x82\xd1\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd0\xbf\xd1\x83\xd1\x81\xd0\xba')),
                ('email', models.EmailField(default=b'', max_length=254, verbose_name=b'Email')),
                ('time_of_reg', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('time_of_coming', models.DateTimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbf\xd0\xbe\xd1\x81\xd0\xb5\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('event_id', models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x80\xd0\xbe\xd0\xbf\xd1\x80\xd0\xb8\xd1\x8f\xd1\x82\xd0\xb8\xd0\xb5', to='newscontent.Event')),
                ('user_id', models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event_registration',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x98\xd0\xbd\xd0\xb4\xd1\x83\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x8f')),
                ('title_eng', models.CharField(max_length=255, verbose_name=b'Industry')),
            ],
            options={
                'db_table': 'industry',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room', models.CharField(max_length=31, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb0\xd1\x83\xd0\xb4\xd0\xb8\xd1\x82\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8')),
                ('picture', models.FileField(null=True, upload_to=newscontent.models.adress_directory_picture_upload, blank=True)),
                ('capacity', models.IntegerField(null=True, verbose_name=b'\xd0\x92\xd0\xbc\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True)),
            ],
            options={
                'db_table': 'room_adress',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=31, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('surname', models.CharField(max_length=31, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('name_en', models.CharField(max_length=31, verbose_name=b'Name')),
                ('surname_en', models.CharField(max_length=31, verbose_name=b'Surname')),
                ('role', models.CharField(max_length=31, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb7\xd0\xb8\xd1\x86\xd0\xb8\xd1\x8f')),
                ('role_en', models.CharField(max_length=31, verbose_name=b'Role')),
                ('alumni', models.BooleanField(verbose_name=b'\xd0\x92\xd1\x8b\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xbd\xd0\xb8\xd0\xba Keystone')),
                ('alma_mater', models.CharField(max_length=31, verbose_name=b'\xd0\x90\xd0\xbb\xd1\x8c\xd0\xbc\xd0\xb0-\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb5\xd1\x80 \xd0\xb8 \xd0\xb3\xd0\xbe\xd0\xb4')),
                ('alma_mater_en', models.CharField(max_length=31, verbose_name=b'Alma mater')),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('position', models.IntegerField(null=True, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd1\x82\xd0\xb0 \xd0\xb2 \xd1\x81\xd0\xbf\xd0\xb8\xd1\x81\xd0\xba\xd0\xb5', blank=True)),
                ('linkedin', models.URLField(null=True, verbose_name=b'LinkedIn', blank=True)),
                ('vk', models.URLField(null=True, verbose_name=b'VK', blank=True)),
                ('facebook', models.URLField(null=True, verbose_name=b'Facebook', blank=True)),
                ('instagram', models.URLField(null=True, verbose_name=b'Instagram', blank=True)),
                ('city', models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', blank=True, to='newscontent.City', null=True)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='UploadingCV_CL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cv_upload', models.FileField(upload_to=newscontent.models.upload_location, null=True, verbose_name=b'Curriculum Vitae (CV)')),
                ('cover_letter', models.TextField(null=True, verbose_name=b'Cover Letter')),
                ('time_uploaded', models.DateTimeField(auto_now_add=True)),
                ('custom_user', models.ForeignKey(blank=True, to='newscontent.CustomUser', null=True)),
                ('user', models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba \xd0\xb2\xd0\xb0\xd0\xba\xd0\xb0\xd0\xbd\xd1\x81\xd0\xb8\xd0\xb8')),
                ('description', tinymce.models.HTMLField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('department', models.CharField(max_length=127, null=True, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbf\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82', blank=True)),
                ('office_location', models.CharField(max_length=255, null=True, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 \xd0\xbe\xd1\x84\xd0\xb8\xd1\x81\xd0\xb0', blank=True)),
                ('aproved', models.BooleanField(default=False, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd\xd0\xbe \xd0\xba \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('site_apply', models.BooleanField(verbose_name=b'Apply \xd0\xbd\xd0\xb0 \xd1\x81\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb5 Keystone')),
                ('cl_reqired', models.BooleanField(verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd0\xb1\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c CL \xd0\xbe\xd1\x82 \xd0\xba\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb8\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0')),
                ('active', models.BooleanField(default=True, verbose_name=b'\xd0\x90\xd0\xba\xd1\x82\xd1\x83\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xb2\xd0\xb0\xd0\xba\xd0\xb0\xd1\x81\xd0\xb8\xd1\x8f')),
                ('employment_rate', models.CharField(max_length=1, verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xb7\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8', choices=[(b'F', b'Full Time Position'), (b'P', b'Part Time Position'), (b'I', b'Paid Internship'), (b'U', b'Unpaid Internship')])),
                ('expiry_date', models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb5\xd0\xbc\xd0\xb0 \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xbe\xd0\xba', blank=True)),
                ('count_views', models.PositiveIntegerField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd0\xbe\xd0\xb2 \xd0\xb2\xd0\xb0\xd0\xba\xd0\xb0\xd0\xbd\xd1\x81\xd0\xb8\xd0\xb8', blank=True)),
                ('count_applies', models.PositiveIntegerField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe apply', blank=True)),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('publication_date', models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('company', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', to='newscontent.Company')),
                ('field_of_industry', models.ForeignKey(verbose_name=b'\xd0\x98\xd0\xbd\xd0\xb4\xd1\x83\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x8f', to='newscontent.Industry')),
                ('office_city', models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='newscontent.City')),
                ('office_country', models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0', to='newscontent.Country')),
            ],
            options={
                'db_table': 'vacancy',
            },
        ),
        migrations.AddField(
            model_name='uploadingcv_cl',
            name='vacancy',
            field=models.ForeignKey(default=b'', to='newscontent.Vacancy'),
        ),
        migrations.AddField(
            model_name='event',
            name='eventclass_id',
            field=models.ForeignKey(verbose_name=b'\xd0\x9e\xd0\xb4\xd0\xbd\xd0\xb0 \xd0\xb2\xd1\x81\xd1\x82\xd1\x80\xd0\xb5\xd1\x87\xd0\xb0 \xd0\xb8\xd0\xbb\xd0\xb8 \xd0\xba\xd1\x83\xd1\x80\xd1\x81', to='newscontent.EventClass'),
        ),
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.ForeignKey(verbose_name=b'\xd0\x90\xd1\x83\xd0\xb4\xd0\xb8\xd1\x82\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True, to='newscontent.Room', null=True),
        ),
    ]
