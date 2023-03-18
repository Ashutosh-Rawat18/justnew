"""prescribeme2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from index.views import home
# from login.views import login
from choice.views import choice
# from docreg.views import docreg
# from patreg.views import patreg
from contact.views import cont
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    # path('login/', login, name="login")
    path('login/', include('login.urls')),
    path('choice/', choice, name="choice"),
    # path('docreg/', docreg, name="docreg"),
    # path('patreg/', patreg, name="patreg")
    path('patreg/', include('patreg.urls')),
    path('docreg/', views.docreg, name="docreg"),
    # path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/', views.showpre, name="showpre"),
    path('insertpre/', views.insertpre, name="insertpre"),
    path('dashboard/Edit/<int:id>', views.editpre, name="editpre"),
    path('dashboard/Update/<int:id>', views.updatepre, name="updatepre"),
    path('dashboard/Delete/<int:id>', views.delpre, name="delpre"),
    path('contact/', cont, name="cont"),

]
