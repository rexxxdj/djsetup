"""djsetup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from mainpage import views as mainview
#from mainpage.views import MainPage
from news import views as newsview
from about.views import FeedbackView
from djsetup import settings


urlpatterns = [
	url(r'^$', mainview.main_page, name='home'),
	url(r'^news/$', newsview.news_list, name='news'),
    url(r'^news/(?P<pk>\d+)/$', newsview.news_detail, name='detail'),
    url(r'^about/$', FeedbackView.as_view(), name='about'),


    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	url(r'^admin/', admin.site.urls),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
