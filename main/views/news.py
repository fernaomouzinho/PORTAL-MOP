import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from customs.utils import month_name_to_number
from main.utils_lang import lang_master
from news.models import News, NewsImage, NewsCat
from about.models import About, Contact
from custom.utils import *
from main.models import Languague

def detailNews(request, lang, year, month, hashid, titleseo):
    objects = get_object_or_404(News, hashed=hashid)
    lang_data = lang_master(lang)
    images = NewsImage.objects.filter(news=objects)
    image = NewsImage.objects.filter(news=objects).first()
    about = About.objects.first()
    contact = Contact.objects.first()
    if image: img = image.image.url
    else: img = "/main/static/main/img/logo-mop.pmg"
    headline_tt = objects.headline_tt[:50]
    headline_pt = objects.headline_pt[:50]
    headline_en = objects.headline_en[:50]
    fb = [objects.title_tt,objects.title_pt,objects.title_en,headline_tt,headline_pt,headline_en,img]
    
    if lang == "tt":
        path_news_yr_mt_hs_ti_tt=request.path
        legend = "Detalla"
        context = {
            'objects': objects, 'images': images, 'news_active': "active", 'fb': fb,'year':year, 'month':month,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'path_news_yr_mt_hs_ti_tt':path_news_yr_mt_hs_ti_tt,
            'title': legend, 'legend': legend
        }
    elif lang == "pt":
        path_news_yr_mt_hs_ti_pt=request.path
        legend = "Detalha"
        context = {
            'objects': objects, 'images': images, 'news_active': "active", 'fb': fb,'year':year,'month':month,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'path_news_yr_mt_hs_ti_pt':path_news_yr_mt_hs_ti_pt,
            'about': about, 'contact': contact,
            'title': legend, 'legend': legend
        }
    else:
        path_news_yr_mt_hs_ti_en=request.path
        legend = "Details"
        context = {
            'objects': objects, 'images': images, 'news_active': "active", 'fb': fb,'year':year,'month':month,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en','path_news_yr_mt_hs_ti_en':path_news_yr_mt_hs_ti_en,
            'about': about, 'contact': contact,
            'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/news_detail.html', context)


def listNews(request, lang):
    about = About.objects.first()
    contact = Contact.objects.first()
    news_group = News.objects.filter(is_active=True).distinct().values('date__year').all()
    queryset_list = News.objects.filter(is_active=True).all().order_by('-date')
    lang_data = lang_master(lang)
    
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
        (Q(title__icontains=query))).distinct()
    else:
        queryset_list = queryset_list
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if lang == "tt":
        path_news_li_tt=request.path
        legend = "Nutisia"
        search = "Buka notisia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'path_news_li_tt':path_news_li_tt,
            'search': search, 'title': legend, 'legend': legend
        }
    elif lang == "pt":
        path_news_li_pt=request.path
        legend = "Notícia"
        search = "Procurar notícia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'path_news_li_pt':path_news_li_pt,
            'search': search, 'title': legend, 'legend': legend
        }
    else:
        path_news_li_en=request.path
        legend = "News"
        search = "Search for news"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang,'l3': 'en','path_news_li_en':path_news_li_en,
            'search': search, 'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/news_list.html', context)

def listCatNews(request, lang, cat):
    about = About.objects.first()
    contact = Contact.objects.first()
    cat_news=NewsCat.objects.filter(slug_name_en=cat).values('name_tt','name_pt','name_en').first()
    news_group = News.objects.filter(is_active=True, cat__slug_name_en=cat).distinct().values('date__year').all()
    queryset_list = News.objects.filter(is_active=True, cat__slug_name_en=cat).all().order_by('-date')
    lang_data = lang_master(lang)
    query = request.GET.get("q")
    if lang == "tt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_tt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    elif lang == "pt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_pt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_en__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    if lang == "tt":
        path_news_cat_tt = request.path
        legend = f"Nutisia {cat_news['name_tt']}" 
        search = "Buka nutisia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'cat':cat,
            'search': search, 'title': legend, 'legend': legend, 'path_news_cat_tt':path_news_cat_tt,
        }
    elif lang == "pt":
        path_news_cat_pt = request.path
        legend = f"Notícia {cat_news['name_pt']}" 
        search = "Procurar notícia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'cat':cat,
            'search': search, 'title': legend, 'legend': legend, 'path_news_cat_pt':path_news_cat_pt,
        }
    else:
        path_news_cat_en = request.path
        legend = f"{cat_news['name_en']} News" 
        search = "Search for news"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'cat':cat,
            'search': search, 'title': legend, 'legend': legend, 'path_news_cat_en':path_news_cat_en,
        }
    return render(request, 'inner_pages/news_cat_list.html', context)


def listCatNewsYear(request, lang, cat, year):
    about = About.objects.first()
    contact = Contact.objects.first()
    cat_news=NewsCat.objects.filter(slug_name_en=cat).values('name_tt','name_pt','name_en').first()
    news_group = News.objects.filter(is_active=True, cat__slug_name_en=cat, date__year=year).distinct().values('date__year', 'date__month','cat').all()
    queryset_list = News.objects.filter(is_active=True, cat__slug_name_en=cat,  date__year=year).all().order_by('-date')
    lang_data = lang_master(lang)
    query = request.GET.get("q")
    if lang == "tt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_tt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    elif lang == "pt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_pt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_en__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
    news_month = []
    if lang == "tt":
        path_news_cat_yr_tt = request.path
        for i in news_group:
            m = f_monthname_tet(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"Nutisia {cat_news['name_tt']} {year}" 
        search = "Buka notisia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'cat':cat,'year':year,'news_month': news_month,
            'search': search, 'title': legend, 'legend': legend, 'path_news_cat_yr_tt':path_news_cat_yr_tt,
        }
    elif lang == "pt":
        path_news_cat_yr_pt = request.path
        for i in news_group:
            m = f_monthname_por(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"Notícia {cat_news['name_tt']} {year}" 
        search = "Procurar notícia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'cat':cat,'year':year,'news_month': news_month,
            'search': search, 'title': legend, 'legend': legend, 'path_news_cat_yr_pt':path_news_cat_yr_pt,
        }
    else:
        path_news_cat_yr_en = request.path
        for i in news_group:
            m = f_monthname_eng(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"{cat_news['name_tt']} News,  {year}" 
        search = "Search for news"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'news_group': news_group,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'cat':cat,'year':year,'news_month': news_month,
            'search': search, 'title': legend, 'legend': legend, 'path_news_cat_yr_en':path_news_cat_yr_en,
        }
    return render(request, 'inner_pages/news_cat_year_list.html', context)

def listCatNewsYearMonth(request,lang,cat,year,month):
    about = About.objects.first()
    contact = Contact.objects.first()
    cat_news=NewsCat.objects.filter(slug_name_en=cat).values('name_tt','name_pt','name_en').first()
    mt=str(month).capitalize()
    month_number = month_name_to_number(mt)
    news_group = News.objects.filter(is_active=True, cat__slug_name_en=cat, date__year=year).distinct().values('date__year','date__month','cat').all()
    queryset_list = News.objects.filter(is_active=True, cat__slug_name_en=cat, date__year=year, date__month=month_number).all().order_by('-date')
        
    lang_data = lang_master(lang)
    
    query = request.GET.get("q")
    if lang == "tt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_tt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    elif lang == "pt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_pt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_en__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    news_month = []
    
    if lang == "tt":
        path_news_cat_yr_mt_tt= request.path
        month_name = f_monthname_tet(int(month_number))+" "+year
        for i in news_group:
            m = f_monthname_tet(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"Nutisia {cat_news['name_tt']}, {month_name}"
        search = "Buka notisia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact,'legend':legend,
            'year': year, 'news_month': news_month, 'month_name': month_name, 'month':month,'cat':cat,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt','path_news_cat_yr_mt_tt':path_news_cat_yr_mt_tt
        }
    elif lang == "pt":
        path_news_cat_yr_mt_pt= request.path
        month_name = f_monthname_por(int(month_number))+" de "+year
        for i in news_group:
            m = f_monthname_por(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"Notícia {cat_news['name_pt']}, {month_name}"
        search = "Procurar notícia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact,
            'year': year, 'news_month': news_month, 'month_name': month_name,'month':month,'cat':cat,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'path_news_cat_yr_mt_pt':path_news_cat_yr_mt_pt,
            'search': search, 'title': legend, 'legend': legend
        }
    else:
        path_news_cat_yr_mt_en= request.path
        month_name = f_monthname_eng(int(month_number))+", "+year
        for i in news_group:
            m = f_monthname_eng(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"{cat_news['name_en']} News of {month_name}"
        search = "Search for news"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact,
            'year': year, 'news_month': news_month, 'month_name': month_name,'month':month,'cat':cat,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'path_news_cat_yr_mt_en':path_news_cat_yr_mt_en,
            'search': search, 'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/news_cat_year_month_list.html', context)

def listNewsYear(request,lang,year):
    about = About.objects.first()
    contact = Contact.objects.first()
    news_group = News.objects.filter(is_active=True, date__year=year).distinct().values('date__year', 'date__month').all()
    queryset_list = News.objects.filter(is_active=True, date__year=year).all().order_by('-date')
    
    lang_data = lang_master(lang)
    query = request.GET.get("q")
    if lang == "tt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_tt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    elif lang == "pt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_pt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_en__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
    news_month = []
    if lang == "tt":
        path_news_yr_tt= request.path
        for i in news_group:
            m = f_monthname_tet(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"Notisia Tinan {year}"
        search = "Buka notisia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'year': year, 'news_month': news_month,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'path_news_yr_tt':path_news_yr_tt, 
            'search': search, 'title': legend, 'legend': legend
        }
    elif lang == "pt":
        path_news_yr_pt= request.path
        for i in news_group:
            m = f_monthname_por(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"Notícia do Ano de {year}"
        search = "Procurar notícia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'year': year, 'news_month': news_month,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt','path_news_yr_pt':path_news_yr_pt, 
            'search': search, 'title': legend, 'legend': legend
        }
    else:
        path_news_yr_en= request.path
        for i in news_group:
            m = f_monthname_eng(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"News of {year}"
        search = "Search for news"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact, 'year': year, 'news_month': news_month,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'path_news_yr_en':path_news_yr_en,
            'search': search, 'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/news_list_year.html', context)


def listNewsMonth(request,lang,year,month):
    about = About.objects.first()
    contact = Contact.objects.first()
    obj_lang =Languague.objects.filter(abrev=lang)
    ol=str(obj_lang[0]).capitalize()
    mt=str(month).capitalize()
    month_number = month_name_to_number(mt)
   
    news_group = News.objects.filter(is_active=True, date__year=year).distinct().values('date__year','date__month').all()
    queryset_list = News.objects.filter(is_active=True, date__year=year, date__month=month_number).all().order_by('-date')
        
    lang_data = lang_master(lang)
    
    query = request.GET.get("q")
    if lang == "tt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_tt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    elif lang == "pt":
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_pt__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        if query:
            queryset_list = queryset_list.filter(
            (Q(title_en__icontains=query))).distinct()
        else:
            queryset_list = queryset_list
        paginator = Paginator(queryset_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    news_month = []
    
    if lang == "tt":
        path_news_yr_mt_tt= request.path
        month_name = f_monthname_tet(int(month_number))+" "+year
        for i in news_group:
            m = f_monthname_tet(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"Notisia Fulan {month_name}"
        search = "Buka notisia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact,
            'year': year, 'news_month': news_month, 'month_name': month_name, 'month':month,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt','path_news_yr_mt_tt':path_news_yr_mt_tt,
            'search': search, 'title': legend, 'legend': legend
        }
    elif lang == "pt":
        path_news_yr_mt_pt= request.path
        month_name = f_monthname_por(int(month_number))+" de "+year
        for i in news_group:
            m = f_monthname_por(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"Notícia do Mês de  {month_name}"
        search = "Procurar notícia"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact,
            'year': year, 'news_month': news_month, 'month_name': month_name,'month':month,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'path_news_yr_mt_pt':path_news_yr_mt_pt,
            'search': search, 'title': legend, 'legend': legend
        }
    else:
        path_news_yr_mt_en= request.path
        month_name = f_monthname_eng(int(month_number))+", "+year
        for i in news_group:
            m = f_monthname_eng(i['date__month'])
            ms = str(m).lower()
            news_month.append([i,m,ms])
        legend = f"News of {month_name}"
        search = "Search for news"
        context = {
            'page_obj': page_obj, 'news_active': "active", 'about': about, 'contact': contact,
            'year': year, 'news_month': news_month, 'month_name': month_name,'month':month,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'path_news_yr_mt_en':path_news_yr_mt_en,
            'search': search, 'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/news_list_month.html', context)


