"""djangotestproject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from profileportal.views import index,login_user,register,logout_user,details


urlpatterns = [
    
    url(r'^$',index,name='index'),
    url(r'^login_user/$',login_user,name='login_user'),
    url(r'^register/$',register,name="register"),
    url(r'^logout_user/$',logout_user,name='logout_user'),
    url(r'^admin/', admin.site.urls),
    url(r'^details/$',details,name='details')
]
