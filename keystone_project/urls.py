"""keystone_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static #adding static
from django.contrib import admin
import newscontent
import keystone_project
from newscontent import views
from keystone_project import views

urlpatterns = [
    url(r'^$', newscontent.views.home, name="home"),
    # url(r'^contact/$', newscontent.views.contact, name="contact"),
    url(r'^about/$', newscontent.views.about, name="about"),
    url(r'^why/$', newscontent.views.why, name="why"),
    url(r'^developing/$', newscontent.views.dev_page, name="developing"),
    url(r'^accounts/', include('allauth.urls')),

    #url(r'^blog/', include('blog.urls'))

    url(r'^admin/', include(admin.site.urls)),
    url(r'^personal_account/$', newscontent.views.personal_account, name="personal_account"),
    url(r'^personal_account/responses/(?P<id>\d+)/$', newscontent.views.vacancy_responses, name="vacancy_responses"),
    url(r'^vacancies/$', newscontent.views.vacancy_articles, name="vacancy_articles"),
    url(r'^vacancy/(?P<id>\d+)/$', newscontent.views.vacancy_article, name="vacancy_article"),
    url(r'^vacancy/(?P<id>\d+)/response/$', newscontent.views.response, name="response"),
    url(r'^vacancy/(?P<id>\d+)/response/success$', newscontent.views.response_success, name="vacancy_response_success"),
    url(r'^events/$', newscontent.views.event_articles, name="event_articles"),
    url(r'^event/(?P<id>\d+)/$', newscontent.views.event_article, name="event_article"),
    url(r'^event/(?P<id>\d+)/response/$', newscontent.views.event_response, name="event_response"),
    url(r'^event/(?P<id>\d+)/response/success$', newscontent.views.event_response_success, name="event_registration_completed"),
    url(r'^career/$', newscontent.views.career, name="career"),
    url(r'^topics/$', newscontent.views.topics, name="topics"),
    url(r'^media/(?P<user_id>\d+)/cv/(?P<user_directory>.*)', newscontent.views.show_cv_file),
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
	 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)