from django.shortcuts import render
from main.utils_lang import lang_master
from about.models import Contact, About
from project.models import PortalHome, ProjCat, ProjCap, ProjSec, ProjMapG, ProjMapS, ProjMapP
from project.read_api import read_cont_list, read_cont_hist

def ProjSum(request, lang):
	if lang == "pt": legend = "Sumário Projeto"
	elif lang == "en": legend = "Project Summary"
	else: legend = "Sumariu Projetu"
	lang_data = lang_master(lang)
	about = About.objects.first()
	contact = Contact.objects.first()
	data_status = PortalHome.objects.filter(is_active=True).first()
	data_cat = ProjCat.objects.filter(is_active=True).first()
	data_cap = ProjCap.objects.filter(is_active=True).first()
	data_sec = ProjSec.objects.filter(is_active=True).first()
	context = {
		'proj_active':"active", 'about':about, 'contact':contact, 'lang_data':lang_data,
		'lang':lang, 'l1':'tt', 'l2':'pt', 'l3':'en',
		'data_status':data_status, 'data_cat':data_cat, 'data_cap':data_cap, 'data_sec':data_sec, 
		'title': legend, 'legend': legend
	}
	return render(request, 'inner_pages/proj_sum.html', context)

def ProjList(request, lang):
	if lang == "pt": legend = "Lista dos Projetos"
	elif lang == "en": legend = "List of Ongoing Projects"
	else: legend = "Lista Projetu Nebe Lao Hela"
	lang_data = lang_master(lang)
	about = About.objects.first()
	contact = Contact.objects.first()
	# read = read_cont_list()
	objects = []
	# for i in read['objects']:
	# 	objects.append(i)
	context = {
		'proj_active':"active", 'about':about, 'contact':contact, 'lang_data':lang_data,
		'lang':lang, 'l1':'tt', 'l2':'pt', 'l3':'en',
		'objects':objects, 
		'title': legend, 'legend': legend
	}
	return render(request, 'inner_pages/proj_list.html', context)

def ProjHist(request, lang):
	if lang == "pt": legend = "Lista dos Projetos Completos"
	elif lang == "en": legend = "List of Completed Projects"
	else: legend = "Lista Projetu Nebe Kompleto Ona"
	lang_data = lang_master(lang)
	about = About.objects.first()
	contact = Contact.objects.first()
	# read = read_cont_hist()
	objects = []
	# for i in read['objects']:
	# 	objects.append(i)
	context = {
		'proj_active':"active", 'about':about, 'contact':contact, 'lang_data':lang_data,
		'lang':lang, 'l1':'tt', 'l2':'pt', 'l3':'en',
		'objects':objects, 
		'title': legend, 'legend': legend
	}
	return render(request, 'inner_pages/proj_list.html', context)
#
def ProjMapGView(request, lang):
	if lang == "pt": legend = "Localização dos Projetos"
	elif lang == "en": legend = "Project Locations"
	else: legend = "Localizasaun Projetu"
	lang_data = lang_master(lang)
	about = About.objects.first()
	contact = Contact.objects.first()
	objects = ProjMapG.objects.filter(is_active=True).first()
	context = {
		'proj_active':"active", 'about':about, 'contact':contact, 'lang_data':lang_data,
		'lang':lang, 'l1':'tt', 'l2':'pt', 'l3':'en',
		'objects':objects, 
		'title': legend, 'legend': legend
	}
	return render(request, 'inner_pages/proj_map_g.html', context)

def ProjMapSView(request, lang):
	if lang == "pt": legend = "Estado dos Projetos"
	elif lang == "en": legend = "Project Status"
	else: legend = "Status Projetu"
	lang_data = lang_master(lang)
	about = About.objects.first()
	contact = Contact.objects.first()
	objects = ProjMapS.objects.filter(is_active=True).first()
	context = {
		'proj_active':"active", 'about':about, 'contact':contact, 'lang_data':lang_data,
		'lang':lang, 'l1':'tt', 'l2':'pt', 'l3':'en',
		'objects':objects, 
		'title': legend, 'legend': legend
	}
	return render(request, 'inner_pages/proj_map_s.html', context)

def ProjMapPView(request, lang):
	if lang == "pt": legend = "Progresso dos Projetos"
	elif lang == "en": legend = "Project Progress"
	else: legend = "Progresu Projetu"
	lang_data = lang_master(lang)
	about = About.objects.first()
	contact = Contact.objects.first()
	objects = ProjMapP.objects.filter(is_active=True).first()
	context = {
		'proj_active':"active", 'about':about, 'contact':contact, 'lang_data':lang_data,
		'lang':lang, 'l1':'tt', 'l2':'pt', 'l3':'en',
		'objects':objects, 
		'title': legend, 'legend': legend
	}
	return render(request, 'inner_pages/proj_map_p.html', context)