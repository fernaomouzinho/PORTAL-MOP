import os
import datetime
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from portal.utils import get_roles
from django.contrib import messages
from news.models import News, NewsImage
from news.forms import NewsForm, NewsImageForm
from news.utils import getnewid, title_seo, log_news, log_newsimage
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsList(request):
    roles = get_roles(request)
    objects = News.objects.all().order_by('-is_headline','-is_main','-datetime')
    context = {
        'group': roles, 'objects': objects,
        'title': 'Nutisia', 'legend': 'Nutisia'
    }
    return render(request, 'news/list.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsAdd(request):
    if request.method == 'POST':
        newid, new_hashid = getnewid(News)
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.slug_title_tt = title_seo(form.cleaned_data.get('title_tt'))
            instance.slug_title_pt = title_seo(form.cleaned_data.get('title_pt'))
            instance.slug_title_en = title_seo(form.cleaned_data.get('title_en'))
            instance.datetime = datetime.datetime.now()
            instance.user = request.user
            instance.hashed = new_hashid
            instance.save()
            messages.success(request, f'Aumenta ona.')
            return redirect('admin-news-det', hashid=new_hashid)
    else: form = NewsForm()
    context = {
        'form': form,
        'title': 'Aumenta Noticia', 'legend': 'Aumenta Noticia'
    }
    return render(request, 'news/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsEdit(request, hashid):
    objects = get_object_or_404(News, hashed=hashid)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.entered_date = datetime.datetime.now()
            instance.entered_by = request.user
            instance.save()
            messages.success(request, f'Altera ona.')
            return redirect('admin-news-det', hashid=hashid)
    else: form = NewsForm(instance=objects)
    context = {
        'objects': objects, 'form': form,
        'title': 'Altera Noticia', 'legend': 'Altera Noticia'
    }
    return render(request, 'news/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsDetail(request, hashid):
    roles = get_roles(request)
    news = get_object_or_404(News, hashed=hashid)
    images = NewsImage.objects.filter(news=news).all()
    context = {
        'group': roles, 'news': news, 'images': images,
        'title': 'Detalha Noticia', 'legend': 'Detalha Noticia'
    }
    return render(request, 'news/detail.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsRem(request, pk):
    objects = get_object_or_404(News, pk=pk)
    if request.method == 'GET':
        objects.delete()
        messages.success(request, f'Hapaga ona')
        return redirect('admin-news-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsEnable(request, hashid):
    objects = get_object_or_404(News, hashed=hashid)
    if request.method == 'GET':
        objects.is_active = True
        objects.save()
        messages.success(request, f'Ativa ona')
        return redirect('admin-news-det', hashid=hashid)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsDisable(request, hashid):
    objects = get_object_or_404(News, hashed=hashid)
    if request.method == 'GET':
        objects.is_active = False
        objects.save()
        messages.success(request, f'Desativa ona')
        return redirect('admin-news-det', hashid=hashid)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsMainYes(request, pk):
    objects = get_object_or_404(News, pk=pk)
    objects.is_main = True
    objects.save()
    messages.success(request, f'Main yes')
    return redirect('admin-news-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsMainNo(request, pk):
    objects = get_object_or_404(News, pk=pk)
    objects.is_main = False
    objects.save()
    messages.success(request, f'Main no')
    return redirect('admin-news-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsHeadline(request, pk):
    objects = get_object_or_404(News, pk=pk)
    objects.is_headline = True
    objects.save()
    objects2 = News.objects.exclude(pk=pk)
    for i in objects2:
        i.is_headline = False
        i.save()
    messages.success(request, f'Headline okay')
    return redirect('admin-news-list')
###

@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsImageAdd(request, hashid):
    objects = get_object_or_404(News, hashed=hashid)
    if request.method == 'POST':
        newid, new_hashid = getnewid(NewsImage)
        form = NewsImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.news = objects
            instance.datetime = datetime.datetime.now()
            instance.user = request.user
            instance.hashed = new_hashid
            instance.save()
            messages.success(request, f'Aumenta ona.')
            return redirect('admin-news-det', hashid=hashid)
    else: form = NewsImageForm()
    context = {
        'hashid': hashid, 'objects': objects, 'form': form,
        'title': 'Aumenta Imajen', 'legend': 'Aumenta Imajen'
    }
    return render(request, 'news/form_image.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def NewsImageEdit(request, hashid, pk):
    objects = get_object_or_404(NewsImage, pk=pk)
    if request.method == 'POST':
        form = NewsImageForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, f'Altera ona.')
            return redirect('admin-news-det', hashid=hashid)
    else: form = NewsImageForm(instance=objects)
    context = {
        'hashid': hashid, 'objects': objects, 'form': form,
        'title': 'Altera Imajen', 'legend': 'Altera Imajen'
    }
    return render(request, 'news/form_image.html', context)
