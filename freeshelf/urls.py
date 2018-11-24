
"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from bookshelf import views
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordChangeDoneView,                      PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, )

from django.conf.urls.static import static
from django.conf import settings
# from bookshelf.backends import MyRegistrationView

urlpatterns = [

    path('', views.index, name="home"),

    # path('books/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('books/<slug>/', views.book_detail, name='book_detail'),
    path('books/<slug>/comment/', views.comment_book, name='comment_book'),
    path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),

    path('browse/name/', views.browse_by_name, name='browse'),
    path('browse/name/<initial>/', views.browse_by_name, name='browse_by_name'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
