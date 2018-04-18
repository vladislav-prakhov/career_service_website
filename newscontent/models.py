# coding: utf8
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django import forms
from django.forms.models import modelform_factory
from django.contrib.contenttypes.fields import GenericRelation
from django.dispatch import receiver
import PIL
from allauth.account.models import EmailAddress
import datetime
from tinymce.models import HTMLField


# Create your models here.
# class SignUp(models.Model):
# 	email = models.EmailField()
# 	fname = models.CharField(max_length=127, default="")
# 	lname = models.CharField(max_length=127, default="")
# 	full_name = models.CharField(max_length=127,blank=True, null=True)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

# 	def __unicode__(self):#Python 3.3__str__
# 		return self.email


def company_directory_logo_upload(instance, filename):
	return 'companies/company_{0}/logo/{1}'.format(instance.id, filename)

class Country(models.Model):
    class Meta:
        db_table = 'country'
    title = models.CharField("Страна", max_length=255)
    title_eng = models.CharField("Country", max_length=255)

    def __unicode__(self):#Python 3.3__str__
       return unicode(self.title)

class City(models.Model):
    class Meta:
        db_table = 'city'
    title = models.CharField("Город", max_length=255)
    title_eng = models.CharField("City", max_length=255)

    def __unicode__(self):#Python 3.3__str__
       return unicode(self.title)

class Adress(models.Model):
	class Meta:
		db_table = 'adress'
	title = models.CharField("Адрес", max_length=255)
	title_eng = models.CharField("Adress", max_length=255)
	latitude = models.CharField("Широта", max_length=31, null=True, blank=True)
	longitude = models.CharField("Долгота", max_length=31, null=True, blank=True)
	
	def __unicode__(self):#Python 3.3__str__
		return unicode(self.title)
		
class Industry(models.Model):
	class Meta:
		db_table = 'industry'
	title = models.CharField("Индустрия", max_length=255)
	title_eng = models.CharField("Industry", max_length=255)
	
	def __unicode__(self):#Python 3.3__str__
		return unicode(self.title_eng)


def adress_directory_picture_upload(instance, filename):
	return 'adresses/adress_{0}/map_picture/{1}'.format(instance.adress.id, filename)

class Room(models.Model):
    class Meta:
        db_table = 'room_adress'
    room = models.CharField("Номер аудитории", max_length=31)
    picture = models.FileField(upload_to=adress_directory_picture_upload, blank=True, null=True)
    capacity = models.IntegerField("Вместимость", null=True, blank=True)

    def __unicode__(self):#Python 3.3__str__
        return unicode(self.room)

class Company(models.Model):
	class Meta:
		db_table = 'company'
	logo = models.FileField(upload_to=company_directory_logo_upload, blank=True)
	company_name = models.CharField("Название компании", max_length=127, unique=True)
	contact_person = models.CharField("Контактное лицо", max_length=63)
	contact_email = models.EmailField("Контактный email")
	company_type = models.CharField("Тип компании", max_length=31)#BB, PE, VC, CB, MC,  ...
	company_site = models.URLField("Сайт компании", )
	keystone_person_in_charge = models.CharField("Ответственное лицо из команды Keystone", max_length=63)
	added_date = models.DateTimeField("Дата и время добавления", auto_now_add=True, auto_now=False)
	updated = models.DateTimeField("Последнее редактирование", auto_now_add=False, auto_now=True)
	#pass
	def __unicode__(self):#Python 3.3__str__
		return self.company_name


class Vacancy(models.Model):
    class Meta:
        db_table = 'vacancy'

    FULL_TIME = 'F'
    PART_TIME = 'P'
    PAID_INTERNSHIP = 'I'
    UNPAID_INTERNSHIP = 'U'

    RATES = (
        (FULL_TIME, 'Full Time Position'),
        (PART_TIME, 'Part Time Position'),
        (PAID_INTERNSHIP, 'Paid Internship'),
        (UNPAID_INTERNSHIP, 'Unpaid Internship'),
    )

    title = models.CharField("Заголовок вакансии", max_length=40)
    description = HTMLField("Описание") #text field, maximum quantity of chars is not determinded 
    company = models.ForeignKey(Company, verbose_name="Компания") #From db company
    department = models.CharField("Департамент", max_length=127, blank=True, null = True)
    office_country = models.ForeignKey(Country, verbose_name="Страна")
    office_city = models.ForeignKey(City, verbose_name="Город")
    office_location = models.CharField("Адрес офиса", max_length=255, null=True, blank=True)

    aproved = models.BooleanField("Разрешено к публикации", default=False)
    site_apply = models.BooleanField("Apply на сайте Keystone")
    cl_reqired = models.BooleanField("Требовать CL от кандидата")
    active = models.BooleanField("Актуальная вакасия", default = True)

    field_of_industry = models.ForeignKey(Industry, verbose_name="Индустрия")
    employment_rate = models.CharField("Уровень занятости", max_length=1, choices=RATES)
    expiry_date = models.DateTimeField("Дата окончания приема заявок", null=True, blank=True)
    count_views = models.PositiveIntegerField("Количество просмотров вакансии", null=True, blank=True)
    count_applies = models.PositiveIntegerField("Количество apply", null=True, blank=True)

    added_date = models.DateTimeField("Дата и время добавления", auto_now_add=True, auto_now=False)
    publication_date = models.DateTimeField("Дата и время добавления", null=True, blank=True)
    updated = models.DateTimeField("Последнее редактирование", auto_now_add=False, auto_now=True)

    def __unicode__(self):#Python 3.3__str__
        return self.title

#years for graduation
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+6)):
    YEAR_CHOICES.append((r,r))

def user_directory_cv_upload(instance, filename):
	return 'users/{0}/cv/{1}'.format(instance.id, filename)  #work, but not beautiful. Need use CustomUser


def validate_file_extension(value):
	import os
	from django.core.exceptions import ValidationError
	ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
	valid_extensions = ['.pdf']
	if not ext.lower() in valid_extensions:
		raise ValidationError("Пожалуйста, загрузите ваше CV в формате .pdf")

class CustomUser(models.Model):
    class Meta:
        db_table = 'custom_user'

    IS_EMPLOYEE = 'E'
    IS_STAFF = 'S'
    IS_COMPANY = 'C'
    USER_CLASSES = (
        (IS_EMPLOYEE, 'Обычный пользователь'),
        (IS_STAFF, 'Администратор'),
        (IS_COMPANY, 'Компания'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField("Имя",max_length=31)
    surname = models.CharField("Фамилия",max_length=31)
    university = models.CharField("ВУЗ", max_length=127, blank=True, null=True)
    speciality = models.CharField("Факультет",max_length=127, blank=True)
    grad_year = models.IntegerField("Год окончания", max_length=4, choices=YEAR_CHOICES, blank=True, null=True)
    linkedin = models.URLField("LinkedIn",blank=True)
    added_date = models.DateTimeField("Дата и время регистрации", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Последнее редактирование профиля", auto_now_add=False, auto_now=True)
    current_cv = models.FileField("Curriculum Vitae (CV)", upload_to=user_directory_cv_upload, validators=[validate_file_extension], blank=True)
    photo = models.ImageField("Фото", null = True, blank=True)

    company = models.ForeignKey(Company, verbose_name="Компания", default=1)
    user_class = models.CharField("Класс пользователя", max_length=1, choices=USER_CLASSES, default="E")
    
    agree_terms = models.BooleanField("Согласен с условиями пользовательского соглашения", default=False)
    agree_hr = models.BooleanField("Согласен на доступность профиля для HR компаний", default=True)
    
    
    cheked_profile = models.BooleanField("Достоверный профиль", default=False)
    
    def __unicode__(self):#Python 3.3__str__
        return unicode(self.user)
        
        
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
		if created:
			CustomUser.objects.create(user=instance)
			instance.customuser.save()


def upload_location(instance, filename):
    return 'users/{0}/cv/{1}/{2}'.format(instance.vacancy.company.pk,instance.id,filename)

class UploadingCV_CL(models.Model):
	class Meta:
		db_table = 'Applications'
	cv_upload = models.FileField("Curriculum Vitae (CV)", upload_to=upload_location, null=True)
	cover_letter = models.TextField("Cover Letter", null = True)
	user = models.ForeignKey(User, default='')
	custom_user = models.ForeignKey(CustomUser, null=True, blank = True)
	vacancy = models.ForeignKey(Vacancy, default='')
	time_uploaded = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):#Python 3.3__str__
		return unicode(self.user)


class EventClass(models.Model):
	class Meta:
		db_table= 'eventclass'
	choose_type = models.CharField("Одна встреча или курс", max_length=31) #event or course
	updated = models.DateTimeField("Последнее редактирование", auto_now_add=False, auto_now=True)
	# count = models.IntegerField(null=True) #count if course

	def __unicode__(self):#Python 3.3__str__
		return unicode(self.choose_type)


class Event(models.Model):
    class Meta:
        db_table = 'event'
    eventclass_id = models.ForeignKey(EventClass, verbose_name="Одна встреча или курс")
    city = models.ForeignKey(City, verbose_name="Город", null=True, blank=True)
    adress = models.ForeignKey(Adress, verbose_name="Адрес", blank=True)  # address
    room = models.ForeignKey(Room, verbose_name="Аудитория", null=True, blank=True)  # address
    title = models.CharField("Название мероприятия", max_length=40)  # title
    title_eng = models.CharField("Event name", max_length=40)  # title
    description = models.TextField("Описание", null=True)  # description
    description_eng = models.TextField("Description", null=True, blank = True)  # description
    date = models.DateTimeField("Дата и время начала", null=True)  # date and time
    timezone = models.CharField("Часовой пояс", max_length=31, null=True, blank=True)  # location-timezone
    added_date = models.DateTimeField("Дата добавления", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Последнее редактирование", auto_now_add=False, auto_now=True)

    def __unicode__(self):#Python 3.3__str__
        return unicode(self.title)


class EventRegistration(models.Model):
    class Meta:
        db_table = 'event_registration'
    event_id = models.ForeignKey(Event, verbose_name="Мероприятие")
    user_id = models.ForeignKey(User, verbose_name="Пользователь")
    fname = models.CharField("Имя", max_length=31)
    lname = models.CharField("Фамилия", max_length=31)
    permit = models.BooleanField("Заказать пропуск")
    email = models.EmailField("Email", default="")
    time_of_reg = models.DateTimeField("Дата и время регистрации", auto_now_add=True,)
    time_of_coming = models.DateTimeField("Время посещения", null=True, blank=True)

    def __unicode__(self):
        return unicode(self.fname + " " + self.lname)
		
class Team(models.Model):
    class Meta:
        db_table = 'team'
    name = models.CharField("Имя",max_length=31)
    surname = models.CharField("Фамилия",max_length=31)
    name_en = models.CharField("Name",max_length=31)
    surname_en = models.CharField("Surname",max_length=31)
    role = models.CharField("Позиция",max_length=31)
    role_en = models.CharField("Role",max_length=31)
    city = models.ForeignKey(City, verbose_name="Город", null=True, blank=True)
    alumni = models.BooleanField("Выпускник Keystone")
    alma_mater = models.CharField("Альма-матер и год",max_length=31)
    alma_mater_en = models.CharField("Alma mater",max_length=31)
    photo = models.ImageField("Фото", null = True, blank=True)
    position = models.IntegerField("Высота в списке", null = True, blank=True)
    linkedin = models.URLField("LinkedIn", null = True, blank=True)
    vk = models.URLField("VK", null = True, blank=True)
    facebook = models.URLField("Facebook", null = True, blank=True)
    instagram = models.URLField("Instagram", null = True, blank=True)

# class Participant(models.Model):
# 	class Meta:
# 		db_table = 'participant'
# 	reg_id = models.OneToOneField(EventRegistration, unique=True)
# 	time_of_coming = models.DateTimeField("Время посещения")
# 	# , default="2000-01-01 00:00[:00[.000001]][W-SU]")
# 	def __unicode__(self):#Python 3.3__str__
# 		return unicode(self.reg_id)



'''
class MediaModel(models.Model):
    media_file = models.FileField(upload_to='user_media')


MediaForm = modelform_factory(MediaModel)
'''
