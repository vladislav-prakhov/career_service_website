from django.contrib import admin

# Register your models here.
#from someotherapp.models import someotherModel
from .forms import CompanyForm
from .forms import VacancyForm

from .forms import CustomUserForm
from .forms import UploadingCV_CL_Form
from .forms import EventClassForm
from .forms import EventForm

from .forms import CountryForm
from .forms import CityForm
from .forms import AdressForm
from .forms import RoomForm
from .forms import IndustryForm
from .forms import TeamForm


from .forms import EventRegistrationForm
# from .forms import ParticipantForm
from .models import Company
from .models import Vacancy
from .models import CustomUser
from .models import UploadingCV_CL
from .models import EventClass
from .models import City
from .models import Event
from .models import Adress
from .models import Room
from .models import Country
from .models import Industry
from .models import EventRegistration
from .models import Team
# from .models import Participant
#
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for CustomUser model
# which acts a bit like a singleton


class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'CustomUser'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class CompanyAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "logo", "company_name", "contact_person",
		 "contact_email", "company_type", "company_site", "keystone_person_in_charge", "added_date", "updated"]
	form = CompanyForm


class VacancyAdmin(admin.ModelAdmin):
	list_display = ["__unicode__",'title', 'company','department','office_country','office_city',
	    'office_location','aproved','site_apply','cl_reqired','active','field_of_industry',
		'employment_rate','expiry_date','count_views']
	form = VacancyForm


class CustomUserAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "name", "surname", "get_email", "university", "speciality", "linkedin", "current_cv", "company", "added_date", "updated"]
	form = CustomUserForm

	def get_email(self, obj):
		return obj.user.email
	get_email.admin_order_field = 'email'
	get_email.short_description = 'Email'


class UploadingCV_CL_Admin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "vacancy", "cv_upload", "cover_letter"]
	form = UploadingCV_CL_Form


class EventClassAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "choose_type", "updated"]
	form = EventClassForm


class EventAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "eventclass_id", "adress", "room", "title", "date", "timezone", "added_date", "updated"]
	form = EventForm

class CountryAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "title", "title_eng"]
	form = CountryForm

class CityAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "title", "title_eng"]
	form = CityForm

class AdressAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "title", "title_eng", "latitude", "longitude"]
	form = AdressForm

class RoomAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "room", "capacity" , "picture"]
	form = RoomForm
	
class IndustryAdmin(admin.ModelAdmin):
    list_display = ["title", "title_eng"]
    form = IndustryForm

class EventRegistrationAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "event_id", "user_id", "fname", "lname", "permit", "email", "time_of_reg", "time_of_coming"]
	form = EventRegistrationForm
	
	
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "surname",  "name_en", "surname_en", "role", "role_en", "city", "alumni", "alma_mater", "alma_mater_en", "photo","position", "linkedin", "vk", "facebook", "instagram"]
    form = TeamForm

# class ParticipantAdmin(admin.ModelAdmin):
# 	list_display = ["__unicode__","reg_id","time_of_come"]
# 	form = ParticipantForm

admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Industry, IndustryAdmin)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UploadingCV_CL, UploadingCV_CL_Admin)
admin.site.register(EventClass, EventClassAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Adress, AdressAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
admin.site.register(Team, TeamAdmin)

# admin.site.register(Participant, ParticipantAdmin)
