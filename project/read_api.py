import requests
import numpy as np

def read_portal_home():
	try:
		# r = requests.get('http://localhost:8000/api/proj/portal/home/?format=json')
		r = requests.get('https://sigp.mop.gov.tl/api/proj/portal/home/?format=json')
		r = r.json()
		obj = r
	except: obj = []
	return obj
#
def read_proj_mopcat():
	try:
		# r = requests.get('http://localhost:8000/api/proj/portal/mopcat/?format=json')
		r = requests.get('https://sigp.mop.gov.tl/api/proj/portal/mopcat/?format=json')
		r = r.json()
		obj = r
	except: obj = []
	return obj
#
def read_proj_cat():
	try:
		# r = requests.get('http://localhost:8000/api/proj/portal/cat/?format=json')
		r = requests.get('https://sigp.mop.gov.tl/api/proj/portal/cat/?format=json')
		r = r.json()
		obj = r
	except: obj = []
	return obj
#
def read_proj_cap():
	try:
		# r = requests.get('http://localhost:8000/api/proj/portal/cap/?format=json')
		r = requests.get('https://sigp.mop.gov.tl/api/proj/portal/cap/?format=json')
		r = r.json()
		obj = r
	except: obj = []
	return obj
#
def read_proj_sec():
	try:
		# r = requests.get('http://localhost:8000/api/proj/portal/sec/?format=json')
		r = requests.get('https://sigp.mop.gov.tl/api/proj/portal/sec/?format=json')
		r = r.json()
		obj = r
	except: obj = []
	return obj
#
def read_cont_list():
	try:
		# r = requests.get('http://localhost:8000/api/cont/portal/list/?format=json')
		r = requests.get('https://sigp.mop.gov.tl/api/cont/portal/list/?format=json')
		r = r.json()
		obj = r
	except: obj = []
	return obj

def read_cont_hist():
	try:
		# r = requests.get('http://localhost:8000/api/cont/portal/hist/?format=json')
		r = requests.get('https://sigp.mop.gov.tl/api/cont/portal/hist/?format=json')
		r = r.json()
		obj = r
	except: obj = []
	return obj
