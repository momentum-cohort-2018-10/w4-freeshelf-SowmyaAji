
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
from bookshelf.backends import MyRegistrationView
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.index, name="home"),

    # path('books/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('books/<slug>/', views.book_detail, name='book_detail'),
    path('books/<slug>/comment/', views.add_comment_on_book,
         name='add_comment_on_book'),
    path('categories/<slug>/', views.category_more, name='category_more'),
    path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),

    path('browse/name/', views.browse_by_name, name='browse'),
    path('browse/name/<initial>/', views.browse_by_name, name='browse_by_name'),
    # path('browse/author/', views.browse_by_author, name='browse_author'),
    # path('browse/author/<initial>/',
    #      views.browse_by_author, name='browse_by_author'),
    path('accounts/password/change/', PasswordChangeView.as_view(
        template_name='registration/password_change_form.html'), name="password_change"),
    path('accounts/password/change/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'), name="password_change_done"),
    path('accounts/password/reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name="password_reset"),

    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(
         template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
         template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(
         template_name='registration/password_reset_complete.html'),
         name="password_reset_complete"),


 
    path('accounts/', include('registration.backends.simple.urls')),
    # url(r'^book/(?P<pk>\d+)/comment/$',
    #     views.add_comment_on_book, name='add_comment_on_book'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
