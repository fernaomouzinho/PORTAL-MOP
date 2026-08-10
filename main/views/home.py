import datetime
from django.shortcuts import render, get_object_or_404
from main.utils_lang import lang_master
from django.db.models import Q
from custom.models import DG, Division, OtherDiv
from multimedia.models import Banner, Album, Gallery, Video
from news.models import News
from about.models import Contact, About, ContactMun, Partner, Structure
from project.models import PortalHome
from main.models import Languague

def inisiu(request):
    year = datetime.date.today().year
    lang_data = lang_master(lang='tt')
    banners = Banner.objects.filter(is_active=True).all()
    latest = News.objects.filter(is_headline=True).prefetch_related("newsimage").first()
    news = News.objects.filter(is_active=True,is_main=True).exclude(is_headline=True).all().order_by('-date')[:6]
    about = About.objects.first()
    contact = Contact.objects.first()
    album = Album.objects.filter(is_active=True).all().order_by('-datetime')[:3]
    data1 = PortalHome.objects.filter(is_active=True).first()
    title1 = lang_data['LBL_PCAT']
    title2 = lang_data['LBL_PCAP']
    title3 = lang_data['LBL_PSEC']
    partners = Partner.objects.filter(is_active=True).all()
    teams = Structure.objects.filter((Q(pos_id=1)|Q(pos_id=2)|Q(pos_id=5)), is_active=True).all()
    context = {
        'lang_data':lang_data, 'year':year, 'lang':'tt', 'l1':'tt', 'l2':'pt', 'l3':'en',
        'banners':banners, 'contact':contact, 'about':about, 'album':album, 'partners': partners,
        'teams': teams, 'title1':title1, 'title2':title2, 'title3':title3,
        'latest': latest, 'news': news, 'data1': data1, 'home_active': 'active',
    }
    return render(request, 'main/layout.html', context)


def home(request, lang):
    if lang == "pt":
        language = "Portugues"
        legend = "Início"
    elif lang == "en":
        language = "English"
        legend = "Home"
    else:
        language = "Tetum"
        legend = "Varanda"
    year = datetime.date.today().year
    lang_data = lang_master(lang)
    banners = Banner.objects.filter(is_active=True).all()
    latest = News.objects.filter(is_headline=True).prefetch_related("newsimage").first()
    news = News.objects.filter(is_active=True, is_main=True).exclude(is_headline=True).all().order_by('-date')[:6]
    about = About.objects.first()
    contact = Contact.objects.first()
    album = Album.objects.filter(is_active=True).all().order_by('-datetime')[:3]
    data1 = PortalHome.objects.filter(is_active=True).first()
    title1 = lang_data['LBL_PCAT']
    title2 = lang_data['LBL_PCAP']
    title3 = lang_data['LBL_PSEC']
    partners = Partner.objects.filter(is_active=True).all()
    teams = Structure.objects.filter((Q(pos_id=1)|Q(pos_id=2)|Q(pos_id=5)), is_active=True).all()
    context = {
        'lang_data':lang_data, 'year':year, 'lang':lang, 'l1':'tt', 'l2':'pt', 'l3':'en',
        'banners': banners, 'contact':contact, 'about':about, 'album':album, 'partners': partners,
        'teams': teams, 'title1':title1, 'title2':title2, 'title3':title3,
        'latest': latest, 'news': news, 'data1': data1, 'home_active': 'active',
        'title': f'{legend}', 'legend': f'{legend}'
    }
    return render(request, 'main/layout.html', context)
##
def AboutView(request, lang):
    if lang == "tt": legend = "Kona-ba MOP"
    elif lang == "pt": legend = "Sobre MOP"
    else: legend = "About MOP"	
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    fb = []
    context = {
        'about_active': "active", 'about': about, 'contact': contact, 'fb': fb,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend,
    }
    return render(request, 'inner_pages/ab_about.html', context)

def OrgView(request, lang):
    if lang == "tt": legend = "Organograma MOP"
    elif lang == "pt": legend = "Organograma MOP"
    else: legend = "MOP Chart"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = Structure.objects.filter(is_active=True).all().order_by('order')
    fb = []
    context = {
        'objects': objects, 'about_active': "active", 'about': about, 'contact': contact, 
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'page':'orgCharts', 'fb': fb,
        'title': legend, 'legend': legend,		
    }
    return render(request, 'inner_pages/ab_org_charts.html', context)

def DGList(request, lang):
    if lang == "tt": legend = "Diresaun Geral"
    elif lang == "pt": legend = "Direção Gerais"
    else: legend = "General Directors"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = DG.objects.all()
    fb = []
    context = {
        'objects': objects, 'about_active': "active", 'about': about, 'contact': contact, 
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'page':'orgCharts', 'fb': fb,
        'title': legend, 'legend': legend,		
    }
    return render(request, 'inner_pages/ab_dg_list.html', context)

def DGDet(request, pk, lang):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    obj = get_object_or_404(DG, pk=pk)
    obj2 = Structure.objects.filter(dg=obj, is_active=True).first()
    fb = []
    
    
    if lang == "tt": 
        path_dg_det_tt = request.path
        legend = "Diresaun Geral"
        context = {
            'obj': obj, 'obj2': obj2, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'page':'orgCharts', 'fb': fb, 'path_dg_det_tt':path_dg_det_tt,
            'title': legend, 'legend': legend,		
        }
    elif lang == "pt": 
        path_dg_det_pt = request.path
        legend = "Direção Gerais"
        context = {
            'obj': obj, 'obj2': obj2, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'page':'orgCharts', 'fb': fb, 'path_dg_det_pt':path_dg_det_pt,
            'title': legend, 'legend': legend,		
        }
    else: 
        path_dg_det_en = request.path
        legend = "General Directors"
        context = {
            'obj': obj, 'obj2': obj2, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'page':'orgCharts', 'fb': fb,'path_dg_det_en':path_dg_det_en,
            'title': legend, 'legend': legend,		
        }
    return render(request, 'inner_pages/ab_dg_det.html', context)


def DivList(request, lang):
    if lang == "tt": legend = "Diresaun Nacional"
    elif lang == "pt": legend = "Direção Nacional"
    else: legend = "National Directors"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = Division.objects.all()
    fb = []
    context = {
        'objects': objects, 'about_active': "active", 'about': about, 'contact': contact, 
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'page':'orgCharts', 'fb': fb,
        'title': legend, 'legend': legend,		
    }
    return render(request, 'inner_pages/ab_div_list.html', context)

def DivDet(request, pk, lang):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    obj = get_object_or_404(Division, pk=pk)
    obj2 = Structure.objects.filter(div=obj, is_active=True).first()
    fb = []
    
    if lang == "tt": 
        path_div_det_tt = request.path
        legend = "Diresaun"
        context = {
            'obj': obj, 'obj2': obj2, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'page':'orgCharts', 'fb': fb,'path_div_det_tt':path_div_det_tt,
            'title': legend, 'legend': legend,		
        }
    elif lang == "pt": 
        path_div_det_pt = request.path
        legend = "Direções"
        context = {
            'obj': obj, 'obj2': obj2, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'page':'orgCharts', 'fb': fb,'path_div_det_pt':path_div_det_pt,
            'title': legend, 'legend': legend,		
        }
    else: 
        path_div_det_en = request.path
        legend = "Directors"
        context = {
            'obj': obj, 'obj2': obj2, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'page':'orgCharts', 'fb': fb,'path_div_det_en':path_div_det_en,
            'title': legend, 'legend': legend,		
        }
    return render(request, 'inner_pages/ab_div_det.html', context)


def OtDivList(request, lang):
    if lang == "tt": legend = "Instituisaun Tutela"
    elif lang == "pt": legend = "Instituição Guardiã"
    else: legend = "Guardian Institution"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = OtherDiv.objects.all()
    fb = []
    context = {
        'objects': objects, 'about_active': "active", 'about': about, 'contact': contact, 
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'page':'orgCharts', 'fb': fb,
        'title': legend, 'legend': legend,		
    }
    return render(request, 'inner_pages/ab_otdiv_list.html', context)

def OtDivDet(request, pk, lang):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    obj = get_object_or_404(OtherDiv, pk=pk)
    fb = []
    if lang == "tt": 
        path_otdiv_det_tt = request.path
        legend = "Instituisaun Tutela"
        context = {
            'obj': obj, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt','page':'orgCharts', 'fb': fb,'path_otdiv_det_tt':path_otdiv_det_tt,
            'title': legend, 'legend': legend,		
        }
    elif lang == "pt": 
        path_otdiv_det_tt = request.path
        legend = "Instituição Guardiã"
        context = {
            'obj': obj, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'page':'orgCharts', 'fb': fb,'path_otdiv_det_tt':path_otdiv_det_tt,
            'title': legend, 'legend': legend,		
        }
    else: 
        path_otdiv_det_en = request.path
        legend = "Guardian Institution"
        context = {
            'obj': obj, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'page':'orgCharts', 'fb': fb, 'path_otdiv_det_en':path_otdiv_det_en,
            'title': legend, 'legend': legend,		
        }
    return render(request, 'inner_pages/ab_otdiv_det.html', context)

#
def TeamDetail(request, lang, pk ):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    team = get_object_or_404(Structure, pk=pk)
    
    if lang == "tt": 
        path_tm_det_tt = request.path
        legend = "Detalla"
        context = {
            'team': team, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'path_tm_det_tt':path_tm_det_tt,
            'title': legend, 'legend': legend
        }
       
    elif lang == "pt": 
        path_tm_det_pt = request.path
        legend = "Detalhas"
        context = {
            'team': team, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l2': 'pt', 'path_tm_det_pt':path_tm_det_pt,
            'title': legend, 'legend': legend
        }
    else: 
        path_tm_det_en = request.path
        legend = "Details"
        context = {
            'team': team, 'about_active': "active", 'about': about, 'contact': contact, 'pk':pk,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'path_tm_det_en':path_tm_det_en,
            'title': legend, 'legend': legend
        }
       
    return render(request, 'inner_pages/team_det.html', context)
#
def AlbumList(request, lang):
    if lang == "tt": legend = "Album"
    elif lang == "pt": legend = "Álbum"
    else: legend = "Album"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    objects = Album.objects.filter(is_active=True).all().order_by('-datetime')
    context = {
        'objects': objects, 'media_active': "active", 'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'title': legend, 'legend': legend
    }
    return render(request, 'inner_pages/mul_album.html', context)

def GalleryList(request, lang, hashid):
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    album = get_object_or_404(Album, hashed=hashid)
    objects = Gallery.objects.filter(album=album).all().order_by('-datetime')
    if lang == "tt":
        path_gl_li_tt = request.path
        legend = "Imajen"
        legend2 = "Album"
        context = {
            'album': album,'objects': objects, 'media_active': "active", 'about': about, 'contact': contact,'path_gl_li_tt':path_gl_li_tt, 
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'hashid':hashid,
            'legend2': legend2, 'title': legend, 'legend': legend
        }
    elif lang == "pt":
        path_gl_li_pt = request.path
        legend = "Imagem"
        legend2 = "Álbum"
        context = {
            'album': album,'objects': objects, 'media_active': "active", 'about': about, 'contact': contact, 'path_gl_li_pt':path_gl_li_pt,
            'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'hashid':hashid,
            'legend2': legend2, 'title': legend, 'legend': legend
        }
    else:
        path_gl_li_en = request.path
        legend = "Images"
        legend2 = "Album"
        context = {
            'album': album,'objects': objects, 'media_active': "active", 'about': about, 'contact': contact,'path_gl_li_en':path_gl_li_en,
            'lang_data': lang_data, 'lang': lang, 'l3': 'en', 'hashid':hashid,
            'legend2': legend2, 'title': legend, 'legend': legend
        }
    return render(request, 'inner_pages/mul_gallery.html', context)

def GalleryDet(request, lang, hashid):
    gallery = get_object_or_404(Gallery, hashed=hashid)
    lang_data = lang_master(lang)
    contact = Contact.objects.first()
    if lang == "tt":
        path_gl_det_tt=request.path
        desc = gallery.desc_tt
        legend = "Imajen"
        fb = [desc,"",gallery.image.url]
        context = {
            'gallery': gallery, 'contact': contact, 'fb': fb, 'lang_data': lang_data,
            'lang': lang, 'l1': 'tt', 'media_active': "active",'path_gl_det_tt':path_gl_det_tt,
            'title': desc, 'legend': desc, 'legend2': legend, 'hashid':hashid,
        }
    elif lang == "pt":
        path_gl_det_pt=request.path
        desc = gallery.desc_pt
        legend = "Imagen"
        fb = [desc,"",gallery.image.url]
        context = {
            'gallery': gallery, 'contact': contact, 'fb': fb, 'lang_data': lang_data,
            'lang': lang, 'l2': 'pt', 'media_active': "active",'path_gl_det_pt':path_gl_det_pt,
            'title': desc, 'legend': desc, 'legend2': legend, 'hashid':hashid,
        }
    else:
        path_gl_det_en=request.path
        desc = gallery.desc_en
        legend = "Images"
        fb = [desc,"",gallery.image.url]
        context = {
            'gallery': gallery, 'contact': contact, 'fb': fb, 'lang_data': lang_data,
            'lang': lang, 'l3': 'en', 'media_active': "active",'path_gl_det_en':path_gl_det_en,
            'title': desc, 'legend': desc, 'legend2': legend, 'hashid':hashid,
        }
    return render(request, 'inner_pages/mul_gallery_det.html', context)

def VideoList(request, lang):
    if lang == "pt": legend = "Video"
    elif lang == "en": legend = "Video"
    else: legend = "Video"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    videos = Video.objects.filter(is_active=True).all().order_by('-date')
    context = {
        'videos': videos, 'about': about, 'contact': contact, 'lang_data': lang_data,
        'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'media_active': "active",
        'title': legend, 'legend': legend
    }
    return render(request, 'inner_pages/mul_video.html', context)



def ContactView(request, lang):
    if lang == "tt":
        legend = "Kontaktu"
        nacional = "Nasional"
    elif lang == "pt":
        legend = "Contacto"
        nacional = "Nacional"
    else:
        legend = "Contact"
        nacional = "National"
    lang_data = lang_master(lang)
    about = About.objects.first()
    contact = Contact.objects.first()
    contact_mun = ContactMun.objects.all().order_by('mun')
    context = {
        'contact_active': "active", 'contact_mun': contact_mun, 'about': about, 'contact': contact,
        'lang_data': lang_data, 'lang': lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en',
        'nacional': nacional, 'title': legend, 'legend': legend
    }
    return render(request, 'inner_pages/contact.html', context)