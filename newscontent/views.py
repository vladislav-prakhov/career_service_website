# from django.conf import settings
#from django.core.mail import send_mail
from django import forms
import os
import django
from django.contrib import messages
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import CustomUserForm, CustomUserShortForm, SelectVacancy, UploadingCV_CL_ShortForm, EventReg, EventRegistration
from .forms import VacancyCompanyAddForm
from .models import CustomUser, Vacancy, Event, UploadingCV_CL, Team
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import newscontent
from django.core.files import File
import keystone_project
from django.http import HttpResponse, Http404
import datetime as dt
from datetime import datetime
# Create your views here.


def home(request):
    title = "Welcome"
    queryset = Vacancy.objects.filter(active=True, aproved=True).order_by('-added_date')[:5]

    context = {
        "object_list": queryset,
        "title": title,
    }
    return render(request, "home.html", context)

def about(request):
    title = "Team"
    queryset = Team.objects.all().order_by('-position')

    context = {
        "object_list": queryset,
        "title": title,
    }
    return render(request, "about.html", context)
    
def why(request):
    title = "Why"
    queryset = Team.objects.all().order_by('-position')

    context = {
        "object_list": queryset,
        "title": title,
    }
    return render(request, "why.html", context)

def career(request):
	context = {

	}
	return render(request, "company-list.html", context)

def topics(request):
	context = {

	}
	return render(request, "topics.html", context)

def access(request, id):

	object = get_object_or_404(CustomUser, pk=id)

	return serve_file(request, object.file)


def personal_account(request):
	if request.user.is_authenticated():
		# title = 'Personal account'
		user_ID = request.user.pk
		# b = CustomUser.objects.get(id=user_ID)
		u = CustomUser.objects.get(user_id=user_ID)
		if u.user_class == "E":
			form = CustomUserShortForm(request.POST or None, request.FILES or None, instance=u) #instance=u
			if form.is_valid():
				instance = form.save(commit=False)
				name = form.cleaned_data.get("name")
				surname = form.cleaned_data.get("surname")
				university = form.cleaned_data.get("university")
				speciality = form.cleaned_data.get("speciality")
				linkedin = form.cleaned_data.get("linkedin")
				instance.name = name
				instance.surname = surname
				instance.university = university
				instance.speciality = speciality
				instance.linkedin = linkedin
				instance.save()
				return redirect('personal_account')
				if request.method == "POST":
					print request.POST
			# else:
			# 	title = "Critical error"
			webpage = "personal_account.html"
			context = {
				"form": form,
				"webpage": webpage,
				"u": u,
				# "form2": form2,
				# "title": title,
				"user_ID": user_ID,
			}
		if u.user_class == "C":
		     #filter(company=u.company)
			form3 = VacancyCompanyAddForm(request.POST or None) #instance=u
			
			queryset_list = Vacancy.objects.filter(company=u.company)
			apply_list = UploadingCV_CL.objects.all()
			paginator = Paginator(queryset_list, 25) # Show 25 contacts per page

			page = request.GET.get('page')
			try:
				queryset = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				queryset = paginator.page(1)
			except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
				queryset = paginator.page(paginator.num_pages)


			if form3.is_valid():
				tit = form3.cleaned_data.get("title")
				description = form3.cleaned_data.get("description")
				department = form3.cleaned_data.get("department")
				office_country = form3.cleaned_data.get("office_country")
				office_city = form3.cleaned_data.get("office_city")
				office_location = form3.cleaned_data.get("office_location")
				site_apply = form3.cleaned_data.get("site_apply")
				cl_reqired = form3.cleaned_data.get("cl_reqired")
				field_of_industry = form3.cleaned_data.get("field_of_industry")
				employment_rate = form3.cleaned_data.get("employment_rate")
				expiry_date = form3.cleaned_data.get("expiry_date")


				VACRegister = Vacancy.objects.create(company=u.company, title=tit, description=description, department=department,
				office_country=office_country,office_city=office_city, office_location=office_location, site_apply = site_apply, 
				cl_reqired=cl_reqired, field_of_industry=field_of_industry, employment_rate=employment_rate, expiry_date=expiry_date,
				count_views=0, aproved=0, active=1, count_applies=0)
				
				return redirect('personal_account')

			company_name = u.company
			webpage = "personal_account.html"
			context = {
				# "form": form,
				"u": u,
				"company_name": company_name,
				"apply_list": apply_list,
				"webpage": webpage,
				"object_list": queryset,
				"form3": form3,
				# "title": title,
				"user_ID": user_ID,
			}

	else:
		context = {

		}
	return render(request, "personal_account.html", context)

def trfa(a): #noob method DON'T REPEAD!
    if a == "Yes":
        return True
    else:
        return False

def vacancy_articles(request):
    title = 'Vacancies'

    #PARSER ot sponsora Keystone - Microsoft v Indii
    contract1 = trfa(request.POST.get('contract1'))
    contract2 = trfa(request.POST.get('contract2'))
    contract3 = trfa(request.POST.get('contract3'))
    contract4 = trfa(request.POST.get('contract4'))
    contract5 = trfa(request.POST.get('contract5'))
    contract6 = trfa(request.POST.get('contract6'))
    contract7 = trfa(request.POST.get('contract7'))
    
    rate1 = trfa(request.POST.get('rate1'))
    rate2 = trfa(request.POST.get('rate2'))
    rate3 = trfa(request.POST.get('rate3'))
    rate4 = trfa(request.POST.get('rate4'))
    rate5 = trfa(request.POST.get('rate5'))
    rate6 = trfa(request.POST.get('rate6'))
    
    city1 = trfa(request.POST.get('city1'))
    city2 = trfa(request.POST.get('city2'))
    city3 = trfa(request.POST.get('city3'))
    city4 = trfa(request.POST.get('city4'))
    city5 = trfa(request.POST.get('city5'))
    city6 = trfa(request.POST.get('city6'))
    
    if not (contract1 or contract2 or contract3 or contract4 or contract5 or contract6 or contract7):
        contract1 = True
    if not (rate1 or rate1 or rate2 or rate3 or rate4 or rate5 or rate6):
        rate1 = True
    if not (city1 or city2 or city3 or city4 or city5 or city6):
        city1 = True
    a=[]
    if contract1:
        queryset_list = Vacancy.objects.all()
    else:
        if contract2:
            a.append('F')
        if contract3:
            a.append('P')
        if contract4:
            a.append('L')
        if contract5:
            a.append('PI')
        if contract6:
            a.append('UI')
        if contract7:
            a.append('R')
        queryset_list = Vacancy.objects.filter(employment_rate__in=a)
    
    a=[]
    if rate1:
        queryset_list = queryset_list
    else:
        if rate2:
            a.append(2)
        if rate3:
            a.append(1)
        if rate4:
            a.append(3)
        if rate5:
            a.append(4)
        if rate6:
            b = []
            for i in range(4):
                b.append(i)
            for i in a:
                b.remove(i)
                
            queryset_list = queryset_list.exclude(field_of_industry__in=b)
             
        else:
            queryset_list = queryset_list.filter(field_of_industry__in=a)
    
    a=[]
    if city1:
        queryset_list = queryset_list
    else:
        if city2:
            a.append(1)
        if city2:
            a.append(2)
        if city3:
            a.append(3)
        if city4:
            a.append(4) 
        if city5:
            b = []
            for i in range(4):
                b.append(i)
            for i in a:
                b.remove(i)
            queryset_list = queryset_list.exclude(office_city__in=b)
             
        else:
            queryset_list = queryset_list.filter(office_city__in=a)
    #END PARSER ------
    
    #queryset_list = Vacancy.objects.all()
    
    queryset_list = queryset_list.filter(active=True, aproved=True).order_by('-added_date')
    
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": title,
        
        "contract1": contract1,
        "contract2": contract2,
        "contract3": contract3,
        "contract4": contract4,
        "contract5": contract5,
        "contract6": contract6,
        "contract7": contract7,
        
        "rate1": rate1,
        "rate2": rate2,
        "rate3": rate3,
        "rate4": rate4,
        "rate5": rate5,
        "rate6": rate6,
        
        "city1": city1,
        "city2": city2,
        "city3": city3,
        "city4": city4,
        "city5": city5,
        "city6": city6,        
    }
    return render(request, 'vacancy_articles.html', context)


def vacancy_article(request, id=None):
    instance = get_object_or_404(Vacancy, id=id)

    if request.user.is_authenticated():
        user_ID = request.user.pk
        u = CustomUser.objects.get(user_id=user_ID)
        user = UploadingCV_CL.objects.filter(vacancy=id, user=user_ID)
        if not user:
            applied = False
        else:
            applied = True     
    else:
        applied = False
        u = True

    context = {
        "title": instance.title,
        "instance": instance,
        "applied" : applied,
        "u": u,
    }
    return render(request,'vacancy.html', context)


def response(request, id=None):
    if request.user.is_authenticated():
        user_ID = request.user.pk
        u = CustomUser.objects.get(user_id=user_ID)
        user = UploadingCV_CL.objects.filter(vacancy=id, user=user_ID)
        if not user and u.user_class == "E":
            instance = get_object_or_404(Vacancy, id=id)
            user_ID = request.user.pk
            ouruser = get_object_or_404(User, id=user_ID)
            custus = get_object_or_404(CustomUser, user=ouruser)
            u = CustomUser.objects.get(user_id=user_ID)
    
            form = UploadingCV_CL_ShortForm(request.POST or None, request.FILES or None, instance=instance) #instance =instance
            cv = u.current_cv
            # form.fields['cv_upload'].initial = cv
            if request.POST.get("date")=="Yes":
                if form.is_valid() or not instance.cl_reqired:
                    # cv_up = form.cleaned_data.get('cv_upload')
                # 	instance = form.save(commit=False)
                # 	cv_upload = form.cleaned_data.get("cv_upload")
                # 	instance.cv_upload = cv_upload
                # 	instance.save()
                    # return HttpResponseRedirect({% url 'vacancy_articles'%})
        
                    # VacancyRegister = UploadingCV_CL.objects.create(cv_upload=cv_up, cover_letter=cl, user=ouruser, vacancy=instance)
                    if instance.cl_reqired:
                        cl = form.cleaned_data.get('cover_letter')
                        VacancyRegister = UploadingCV_CL.objects.create(cv_upload=cv, cover_letter=cl, user=ouruser, vacancy=instance, custom_user=custus)
                    else:
                        VacancyRegister = UploadingCV_CL.objects.create(cv_upload=cv, user=ouruser, vacancy=instance, custom_user=custus)
                    
                    return redirect('vacancy_article', id=id)
                    # messages.success(request, "Successfully sent")
            else:
                context = {
                    "instance": instance,
                    "form": form,
                }
                return render(request,'response.html', context)
        else:
            raise Http404
    else:
        raise Http404

def response_success(request, id=None):
    instance = get_object_or_404(Vacancy, id=id)
    context = {
        "instance": instance,
    }
    return render(request,'vacancy_apply_complete.html', context)

def event_article(request, id=None):
    instance = get_object_or_404(Event, id=id)
    end_date = instance.date + dt.timedelta(hours=2)
    if request.user.is_authenticated():
        user_ID = request.user.pk
        u = CustomUser.objects.get(user_id=user_ID)
        user = EventRegistration.objects.filter(event_id=id, user_id=user_ID)
        if not user:
            registered = False
        else:
            registered = True     
    else:
        registered = False
        u = True

    context = {
        "title": instance.title,
        "instance": instance,
        "registered": registered,
        "end_date" : end_date,
        "u" : u,
        }
    return render(request,'event.html', context)

def event_articles(request):
	title = 'Events'
	queryset_list = Event.objects.all()
	paginator = Paginator(queryset_list, 5) # Show ..., n) objects per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": title,
	}
	return render(request, 'event_articles.html', context)

def event_response(request, id=None):
    instance = get_object_or_404(Event, id=id)
    if request.user.is_authenticated():
        user_ID = request.user.pk
        ouruser = get_object_or_404(User, id=user_ID)
        u = CustomUser.objects.get(user_id=user_ID)
        fname = u.name
        lname = u.surname
        email = request.user.email
        
        if request.POST.get('checkbox1') == "Yes":
            permit = True
        else:
            permit = False
        
        EveRegister = EventRegistration.objects.create(event_id=instance, user_id=ouruser, fname=fname, lname=lname, email=email, permit=permit)
        return redirect('event_article', id=id)
    else:
        raise Http404
        
        
def event_response_success(request, id=None):
	instance = get_object_or_404(Event, id=id)
	context = {
		"instance": instance,
	}
	return render(request,'event_registration_completed.html', context)


def show_cv_file (request, user_id=0, user_directory=''):
    user_id = int(user_id)
    user_directory = str(user_directory)
    if request.user.is_authenticated or user_id>0:
        if user_id==request.user.id:
            try:
                cv_dir = keystone_project.settings.MEDIA_ROOT +'/employees/' + str(user_id) + '/cv/' + user_directory
                print(cv_dir)
                f = open(cv_dir, 'rb')
                return HttpResponse(f, content_type='application/pdf')
            except:
                raise Http404
        else:
            raise Http404
    else:
        raise Http404

def vacancy_responses (request, id=None):
    vacancy = Vacancy.objects.get(id=id)
    responses = UploadingCV_CL.objects.filter(vacancy_id=id)
    users = CustomUser.objects.filter

    context = {
        "vacancy": vacancy,
        "responses": responses,
    }

    return render(request, 'vacancy_responses.html', context)

def dev_page(request):
	context = {

	}
	return render(request, "developing.html", context)