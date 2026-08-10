import datetime
import numpy as np
from django.db.models import Count, Q
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from project.models import ProjCat, ProjCap, ProjMopCat, ProjSec

class APIProjMopCat(APIView):
	def get(self, request, format=None):
		label,obj1 = list(),list()
		obj = ProjMopCat.objects.first()
		obj1.append([obj.est,obj.r4d,obj.emer,obj.obrassel,obj.menor,obj.bsgsm])
		label = ['EST','R4D','EMER','OBRASSEL','MENOR','BS-GSM']
		data = { 'label': label, 'obj1': obj1, }
		return Response(data)

class APIProjCat(APIView):
	def get(self, request, format=None):
		label,obj1,obj2,obj3 = list(),list(),list(),list()
		obj = ProjCat.objects.first()
		obj1.append(obj.fi)
		obj2.append(obj.lm)
		obj3.append(obj.emer)
		obj = [obj1,obj2,obj3]
		label = ['FI','LM','EMER']
		data = { 'label': label, 'obj': obj, }
		return Response(data)

class APIProjCap(APIView):
	def get(self, request, format=None):
		label,obj1,obj2,obj3 = list(),list(),list(),list()
		obj = ProjCap.objects.first()
		obj1.append(obj.bs)
		obj2.append(obj.cm)
		obj3.append(obj.cd)
		obj = [obj1,obj2,obj3]
		label = ['BS','CM','CD']
		data = { 'label': label, 'obj': obj, }
		return Response(data)

class APIProjSec(APIView):
	def get(self, request, format=None):
		label,obj1 = list(),list()
		obj = ProjSec.objects.first()
		obj1.append([obj.estrada,obj.ponte,obj.cheias,obj.urban,obj.estudu,obj.asset])
		label = ['Estrada','Ponte','Controlo Cheias','Urbanizasaun','Estudu','Asset']
		data = { 'label': label, 'obj1': obj1, }
		return Response(data)
