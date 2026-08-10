import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from custom.models import Year
from announce.models import Announce
from about.models import About, Contact
from pub.models import Publication, Vaga, Tender
from main.utils_lang import lang_master

#
def VagaList(request, lang):
    if lang == "pt": legend = "Vaga"
    elif lang == "en": legend = "Vacancy"
    else: legend = "Vaga"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    queryset_list = Vaga.objects.filter(is_active=True).all().order_by('-id')
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj, 'project_active': "active",'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend, 
    }
    return render(request, 'inner_pages/vaga_list.html', context)

def VagaDetail(request, lang, hashid):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = get_object_or_404(Vaga, hashed=hashid)
    fb = []
    if lang == "tt": 
        path_vg_det_tt = request.path
        legend = "Detalla"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt','fb': fb,'path_vg_det_tt':path_vg_det_tt,
            'title': legend, 'legend': legend
        }
    elif lang == "pt": 
        path_vg_det_pt = request.path
        legend = "Detalha"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang,  'l2': 'pt','fb': fb,'path_vg_det_pt':path_vg_det_pt,
            'title': legend, 'legend': legend
        }
    else: 
        path_vg_det_en = request.path
        legend = "Details"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'fb': fb,'path_vg_det_en':path_vg_det_en,
            'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/vaga_det.html', context)

#
def TenderList(request, lang):
    if lang == "pt": 
        legend = "Aprovisionamento"
        legend_1 = "Informacao Tender"
        legend_2= "Data Publica"
        
    elif lang == "en": 
        legend = "Procurement"
        legend_1 = "Information of Tender"
        legend_2= "Data Publish"
    else: 
        legend = "Aprovisionamentu"
        legend_1 = "Informasaun Tender"
        legend_2= "Data Publika"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    queryset_list = Tender.objects.filter(is_active=True).all().order_by('-id')
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    today = datetime.date.today().strftime('%Y-%m-%d')
    context = {
        'page_obj': page_obj, 'project_active': "active",'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend, 'legend_1':legend_1,'legend_2':legend_2, 'today':today,
    }
    return render(request, 'inner_pages/tender_list.html', context)

def TenderDetail(request, lang, hashid):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = get_object_or_404(Tender, hashed=hashid)
    fb = []
    if lang == "tt": 
        path_td_det_tt = request.path
        legend = "Detalla"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt','fb': fb,'path_td_det_tt':path_td_det_tt,
            'title': legend, 'legend': legend
        }
    elif lang == "pt": 
        path_td_det_pt = request.path
        legend = "Detalha"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang,  'l2': 'pt','fb': fb,'path_td_det_pt':path_td_det_pt,
            'title': legend, 'legend': legend
        }
    else: 
        path_td_det_en = request.path
        legend = "Details"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'fb': fb,'path_td_det_en':path_td_det_en,
            'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/tender_det.html', context)

#
def AnnList(request, lang):
    if lang == "tt":
        language = "Tetum"
        legend = "Anunsiu"
    elif lang == "pt": 
        language = "Portugues"
        legend = "Anúncio"
    else: 
        language = "English"
        legend = "Announcement"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    queryset_list = Announce.objects.filter(language=language, is_active=True).all().order_by('-date')
    today = datetime.date.today()
    queryset_list1 = list()
    for i in queryset_list:
        new = today - i.date
        if new.days == 0:
            new = True
            queryset_list1.append([i,new])
        else:
            new = False
            queryset_list1.append([i,new])
    paginator = Paginator(queryset_list1, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj, 'download_active': "active", 'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend
    }
    return render(request, 'inner_pages/ann_list.html', context)


def AnnDetail(request, lang, hashid):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = get_object_or_404(Announce, hashed=hashid)
    fb = []
    if lang == "tt": 
        path_ann_det_tt = request.path
        legend = "Detalla"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt','fb': fb,'path_ann_det_tt':path_ann_det_tt,
            'title': legend, 'legend': legend
        }
    elif lang == "pt": 
        path_ann_det_pt = request.path
        legend = "Detalha"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang,  'l2': 'pt','fb': fb,'path_ann_det_pt':path_ann_det_pt,
            'title': legend, 'legend': legend
        }
    else: 
        path_ann_det_en = request.path
        legend = "Details"
        context = {
            'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'fb': fb,'path_ann_det_en':path_ann_det_en,
            'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/ann_det.html', context)



#
def PubList(request, lang):
    objects = []
    objects_list = []
    current_year = datetime.datetime.now().year
    if lang == "tt": legend = "Publikasaun"
    elif lang == "pt": legend = "Publicação"
    else: legend = "Publication"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    queryset_list = Publication.objects.filter(is_active=True).all().order_by('-id')
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj, 'project_active': "active",'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend,'objects':objects, 
    }
    return render(request, 'inner_pages/pub_list.html', context)

def PubDetail(request, lang, hashid):
    if lang == "tt": legend = "Detalla"
    elif lang == "pt": legend = "Detalha"
    else: legend = "Details"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = get_object_or_404(Publication, hashed=hashid)
    context = {
        'objects': objects, 'download_active': "active", 'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend
    }
    return render(request, 'inner_pages/pub_det.html', context)


