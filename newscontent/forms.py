# coding: utf8
from django import forms
from django.forms import CharField

from .models import Company
from .models import Vacancy
from .models import CustomUser
from .models import UploadingCV_CL
from .models import Country
from .models import City
from .models import Adress
from .models import Room
from .models import Industry
from .models import EventClass
from .models import Event
from .models import EventRegistration
from .models import Team
from allauth.utils import generate_unique_username

#from allauth.account.forms import SetPasswordField


# from .models import Participant

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['company_name', 'logo', 'contact_person', 'contact_email', 'company_type', 'company_site', 'keystone_person_in_charge']
	#company_id = models.AutoField(primary_key=True)
	def clean_email(self):
		email = self.cleaned_data.get('contact_email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')

		return email 								#make general function in the future

class VacancyForm(forms.ModelForm):
	class Meta:
		model = Vacancy
		fields = ['title', 'description','company','department','office_country','office_city',
		'office_location','aproved','site_apply','cl_reqired','field_of_industry',
		'employment_rate','expiry_date','count_views']

class IndustryForm(forms.ModelForm):
	model = Industry
	list_display = ["title", "title_eng"]

class VacancyCompanyAddForm(forms.ModelForm):
	class Meta:
		model = Vacancy
		fields = ['title', 'description', 'department', 'office_country', 'office_city',
		'office_location', 'site_apply', 'cl_reqired', 'field_of_industry',
		'employment_rate','expiry_date']

class CustomUserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['company', 'name', 'surname', 'university', 'speciality', 'linkedin', 'current_cv', 'user_class']
		def clean_name(self):
			name=self.cleaned_data.get('name')
			return name
		def clean_surname(self):
			surname=self.cleaned_data.get('surname')
			return surname
		def clean_university(self):
			university=self.cleaned_data.get('university')
			return university
		def clean_speciality(self):
			speciality=self.cleaned_data.get('speciality')
			return speciality
		def clean_linkedin(self):
			linkedin=self.cleaned_data.get('linkedin')
			return linkedin

		def clean_current_cv(self):
			current_cv=self.cleaned_data.get('current_cv')
			if not extension == "pdf":
				raise forms.ValidationError("Пожалуйста загрузите ваше CV в формате .pdf")
			return current_cv
		# def clean_linkedin(self):					#isn't working
		# 	linkedin = self.clean_data.get('linkedin')
		# 	linkedin_base, extension = provider.split('.')
		# 	if not linkedin_base == "linkedin":
		# 		raise forms.ValidationError("Please make sure you have written right your linkedin account")
		# 	if not extension == "com":
		# 		raise forms.ValidationError("Please make sure you have written right your linkedin account")
		# 	return linkedin


class CustomUserShortForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['name', 'surname', 'university', 'speciality', 'linkedin', 'current_cv']
		def clean_name(self):
			name=self.cleaned_data.get('name')
			return name
		def clean_surname(self):
			surname=self.cleaned_data.get('surname')
			return surname
		def clean_university(self):
			university=self.cleaned_data.get('university')
			return university
		def clean_speciality(self):
			speciality=self.cleaned_data.get('speciality')
			return speciality
		def clean_linkedin(self):
			linkedin=self.cleaned_data.get('linkedin')
			return linkedin

		def clean_current_cv(self):
			current_cv=self.cleaned_data.get('current_cv')
			if not extension == "pdf":
				raise forms.ValidationError("Пожалуйста загрузите ваше CV в формате .pdf")
			return current_cv


class SelectVacancy(forms.ModelForm):
	class Meta:
		model = Vacancy
		fields = ['title']
		field_name = forms.ModelChoiceField(
			queryset=Vacancy.objects.all().values_list('title'), 
			empty_label="---Choose value---"
			)

# class UploadFileForm(forms.Form):
# 	title = forms.CharField(max_length=50)
# 	file = forms.FileField()


class UploadingCV_CL_Form(forms.ModelForm):
	class Meta:
		model = UploadingCV_CL
		fields = ['user', 'vacancy', 'cv_upload', 'cover_letter']


class UploadingCV_CL_ShortForm(forms.ModelForm):
	class Meta:
		model = UploadingCV_CL
		fields = ['cover_letter']


class EventClassForm(forms.ModelForm):
	model = EventClass
	list_display = ["choose_type"]


class EventForm(forms.ModelForm):
	model = Event
	list_display = ["eventclass_id", "city", "adress", "room", "title", "title_eng", "description", "description_eng", "date"]

class CountryForm(forms.ModelForm):
	model = Country
	list_display = ["title", "title_eng"]

class CityForm(forms.ModelForm):
	model = Adress
	list_display = ["title", "title_eng"]

class AdressForm(forms.ModelForm):
	model = Adress
	list_display = ["title", "title_eng", "latitude", "longitude"]

class RoomForm(forms.ModelForm):
	model = Adress
	list_display = ["room", "capacity", "picture"]

class EventRegistrationForm(forms.ModelForm):
	model = EventRegistration
	list_display = ["event_id", "user_id", "fname", "lname", "permit", "email", "time_of_reg"]

class TeamForm(forms.ModelForm):
	model = Team
	list_display = ["name", "surname",  "name_en", "surname_en", "role", "role_en", "city", "alumni", "alma_mater", "alma_mater_en", "photo","position", "linkedin", "vk", "facebook", "instagram"]

class EventReg(forms.Form):
    fname = forms.CharField(label="Имя")
    lname = forms.CharField(label="Фамилия")
    email = forms.EmailField(label="Email")
    # class ParticipantForm(forms.ModelForm):
    # 	Model = Participant
    # 	list_display = ["reg_id", "time_of_come"]

class SignupForm(forms.Form):
    name = forms.CharField(max_length=31, label='Имя')
    surname = forms.CharField(max_length=31, label='Фамилия')
    agree_hr = forms.BooleanField(initial=True, label="Согласен на доступность профиля для HR компаний", required=False)
    agree_terms = forms.BooleanField(label="Согласен с условиями пользовательского соглашения", required=True, initial=False)
    
    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'agree_hr', 'agree_terms']

    def signup(self, request, user):
        texts = []
        texts.append(self.cleaned_data['email'])
        texts.append(self.cleaned_data['name'])
        texts.append(self.cleaned_data['surname'])
        
        user.username = generate_unique_username(texts)
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']
        user.save()
        
        custom = CustomUser.objects.get(user=user)
        custom.name = self.cleaned_data['name']
        custom.surname = self.cleaned_data['surname']
        custom.agree_hr = self.cleaned_data['agree_hr']
        custom.agree_terms = self.cleaned_data['agree_terms']
        custom.save()
        