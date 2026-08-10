from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from main.utils_lang import lang_master
from doc.models import Doc, Report, ReportOwner
from about.models import Contact, About
from custom.models import Year
from main.models import Languague

def DocList(request, lang):
    if lang == "pt":
        language = "Portugues"
        legend = "Decreto Lei do MOP"
    elif lang == "en":
        language = "English"
        legend = "Law Decree of MOP"
    else:
        language = "Tetum"
        legend = "Dekretu-Lei MOP"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    queryset_list = Doc.objects.filter(language=language, is_active=True).all().order_by('id')
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend
    }
    return render(request, 'inner_pages/doc_list.html', context)

def DocDetail(request, lang, hashid):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = get_object_or_404(Doc, hashed=hashid)
    
    if lang == "tt": 
        path_doc_det_tt = request.path
        legend = "Detalla"
        context = {
            'objects': objects, 'doc_active': "active", 'about': about, 'contact': contact, 'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'page':'docDetail',
            'title': legend, 'legend': legend, 'path_doc_det_tt':path_doc_det_tt,
        }
    elif lang == "pt": 
        path_doc_det_pt = request.path
        legend = "Detalha"
        context = {
        'objects': objects, 'doc_active': "active", 'about': about, 'contact': contact, 'hashid':hashid,
        'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'page':'docDetail',
        'title': legend, 'legend': legend, 'path_doc_det_pt':path_doc_det_pt,
        }
    else: 
        path_doc_det_en = request.path
        legend = "Details"  
        context = {
            'objects': objects, 'doc_active': "active", 'about': about, 'contact': contact, 'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en','page':'docDetail',
            'title': legend, 'legend': legend, 'path_doc_det_en':path_doc_det_en,
        }
    return render(request, 'inner_pages/doc_det.html', context)

#
def ReportList(request, lang):
    if lang == "pt":
        language = "Portugues"
        legend = "Relatorios"
        legend_2= "Atuál"
        legend_3 = "Direção Geral"
        legend_4 = "Arquivo de relatório"
    elif lang == "en":
        language = "English"
        legend = "Reports"
        legend_2 = "Actual"
        legend_3 = "General Direction"
        legend_4 = "Archive Report"
    else:
        language = "Tetum"
        legend = "Relatoriu"
        legend_2 = "Atual"
        legend_3 = "Diresaun"
        legend_4 = "Arkivu Relatoriu"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    queryset_list = Report.objects.filter(language=language, is_active=True).all().order_by('-id')
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend, 'legend_2':legend_2, 'legend_3':legend_3,'legend_4':legend_4,
    }
    return render(request, 'inner_pages/report_list.html', context)

#
def ReportListDg(request, lang, dg):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    obj_lang =Languague.objects.filter(abrev=lang)
    ol=str(obj_lang[0]).capitalize()
    dg=dg
    queryset_list = Report.objects.filter(owner__code=dg, language=ol, is_active=True, ).all().order_by('-id')
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if  lang == "tt":
        path_rep_dg_tt = request.path
        language = "Tetum"
        legend = "Relatoriu"
        legend_1 = "Relatoriu Diresaun"
        legend_2 = "Arkivu Relatoriu"
        legend_3 = "Diresaun"
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt',
            'title': legend, 'legend': legend, 'legend_1':legend_1, 'legend_2':legend_2, 'legend_3':legend_3, 'dg':dg, 'path_rep_dg_tt':path_rep_dg_tt,
        }
    elif lang == "pt":
        path_rep_dg_pt = request.path
        language = "Portugues"
        legend = "Relatorios"
        legend_1 = "Relatório de Direção  " 
        legend_2 ="Arquivo de relatório"
        legend_3 = "Direção"
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'path_rep_dg_pt':path_rep_dg_pt,
            'title': legend, 'legend': legend,'legend_1':legend_1, 'legend_2':legend_2,'legend_3':legend_3,'dg':dg
        }
    else:
        path_rep_dg_en = request.path
        language = "English"
        legend = "Reports"
        legend_1 = "Direction Reports"
        legend_2 ="Report File"
        legend_3 = "Direction"
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'path_rep_dg_en':path_rep_dg_en,
            'title': legend, 'legend': legend,'legend_1':legend_1, 'legend_2':legend_2,'legend_3':legend_3,'dg':dg
        }
 
    return render(request, 'inner_pages/report_list_dg.html', context)


def ReportDetail(request, lang, hashid):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = get_object_or_404(Report, hashed=hashid)
    
    if lang == "tt": 
        path_rep_det_tt = request.path
        legend = "Detalla"
        context = {
            'objects': objects, 'doc_active': "active", 'about': about, 'contact': contact, 'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'page':'docDetail',
            'title': legend, 'legend': legend, 'path_rep_det_tt':path_rep_det_tt,
        }
    elif lang == "pt": 
        path_rep_det_pt = request.path
        legend = "Detalha"
        context = {
        'objects': objects, 'doc_active': "active", 'about': about, 'contact': contact, 'hashid':hashid,
        'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'page':'docDetail',
        'title': legend, 'legend': legend, 'path_rep_det_pt':path_rep_det_pt,
        }
    else: 
        path_rep_det_en = request.path
        legend = "Details"  
        context = {
            'objects': objects, 'doc_active': "active", 'about': about, 'contact': contact, 'hashid':hashid,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en','page':'docDetail',
            'title': legend, 'legend': legend, 'path_rep_det_en':path_rep_det_en,
        }
    return render(request, 'inner_pages/report_det.html', context)

#
def ReportYearList(request, lang, yr):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    obj_lang =Languague.objects.filter(abrev=lang)
    ol=str(obj_lang[0]).capitalize()
    queryset_list = Report.objects.filter(language=ol, is_active=True, date__year=yr).all().order_by('id')
    yr=yr
    single_year = Year.objects.all().filter(year=yr)
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if lang == "tt":
        path_rep_yr_tt = request.path
        language = "Tetum"
        legend = "Relatoriu"
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt','path_rep_yr_tt':path_rep_yr_tt,
            'title': legend, 'legend': legend, 'single_year':single_year, 'yr':yr
        }
    elif lang == "pt":
        path_rep_yr_pt = request.path
        language = "Portugues"
        legend = "Relatorios"
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'path_rep_yr_pt':path_rep_yr_pt,
            'title': legend, 'legend': legend, 'single_year':single_year, 'yr':yr
        }
    else:
        path_rep_yr_en = request.path
        language = "English"
        legend = "Reports"
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en','path_rep_yr_en':path_rep_yr_en,
            'title': legend, 'legend': legend, 'single_year':single_year, 'yr':yr
        }
    return render(request, 'inner_pages/report_list_year.html', context)


def ReportYearListDg(request, lang, yr, dg):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    obj_lang =Languague.objects.filter(abrev=lang)
    ol=str(obj_lang[0]).capitalize()
    dg=dg
    dgu=str(dg).upper()
    yr=yr
    single_year = Year.objects.all().filter(year=yr)
    queryset_list = Report.objects.filter(owner__code=dg, language=ol, is_active=True,date__year=yr).all().order_by('-id')
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if lang == "tt":
        path_rep_dg_yr_tt = request.path
        language = "Tetum"
        legend = "Relatoriu"
        legend_1 = f"Relatoriu Tinan {yr} Diresaun {dgu}"
        legend_2 = f"Arkivu Relatoriu"
        legend_3 = "Diresaun"
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt','path_rep_dg_yr_tt':path_rep_dg_yr_tt,
            'title': legend, 'legend': legend, 'legend_1':legend_1,'legend_2':legend_2, 'legend_3':legend_3, 'single_year':single_year, 'dg':dg,'yr':yr
        }
    elif lang == "pt":
        path_rep_dg_yr_pt = request.path
        language = "Portugues"
        legend = "Relatorios"
        legend_1 = f"Relatório do Ano {yr} de Direção {dgu}"
        legend_2 = f"Arquivo de Relatório"
        legend_3 = "Direção "
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'path_rep_dg_yr_pt':path_rep_dg_yr_pt,
            'title': legend, 'legend': legend, 'legend_1':legend_1,'legend_2':legend_2, 'legend_3':legend_3,'single_year':single_year, 'dg':dg,'yr':yr
        }
    else:
        path_rep_dg_yr_en = request.path
        language = "English"
        legend = "Reports"
        legend_1 = f"{yr} Report of Direction {dgu}"
        legend_2 = f"REPORT FILE"
        legend_3 = "Direction"
        context = {
            'page_obj': page_obj, 'doc_active': "active", 'about': about, 'contact': contact,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en','path_rep_dg_yr_en':path_rep_dg_yr_en,
            'title': legend, 'legend': legend, 'legend_1':legend_1,'legend_2':legend_2, 'legend_3':legend_3,'single_year':single_year, 'dg':dg, 'yr':yr
        }
    return render(request, 'inner_pages/report_list_year_dg.html', context)