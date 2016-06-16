# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from jul.models import Student, Subject, Score
from laba2.forms import SubForm, StudentForm, AddScoreForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import QueryDict
from django.db import models

def AddSubj(request):
	form = SubForm()
	if request.method == 'GET':
		sid = request.GET.get('subj',0)
		name = 'Музыка'
		hours = 0
		editadd = 'Add'
		if sid != 0:
			s = Subject.objects.filter(id = sid)
			if s.exists():
				name = s[0].sub_name
				hours = s[0].sub_hours
				editadd = 'Save'
		form = SubForm(initial={'subject' : name, 'hours': hours, 'sid':sid})
	else:
		form = SubForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			hours = form.cleaned_data['hours']
			sid = form.cleaned_data['sid']
			if request.POST.get('Add','') == 'Add':
				sub = Subject.objects.create(sub_name = subject, sub_hours = hours)
			if request.POST.get('Save','') == 'Save':
				ss = Subject(id = sid, sub_name = subject, sub_hours = hours)
				sub = ss.save()
			if request.POST.get('Delete','') == 'Delete':
				ss = Subject(id=sid, sub_name = subject, sub_hours = hours)
				sub = ss.delete()



			return HttpResponseRedirect('/')
		else:
			editadd=request.POST.get('Add',request.POST.get('Save',request.POST.get('Delete','')))
	return render(request, 'addsubj.html', {'form': form, 'submit': editadd})

def AddStudent(request):
	form = StudentForm()
	if request.method == 'GET':
		stid = request.GET.get('stud',0)
		name = 'Иванов'
		email = '-'
		group = 724
		editadd = 'Add'
		if stid != 0:
			s = Student.objects.filter(id = stid)
			if s.exists():
				name = s[0].name
				email = s[0].email
				group = s[0].group_number
				editadd = 'Save'
		form = StudentForm(initial={'name' : name, 'email': email, 'group_number' : group, 'stid':stid})
	else:
		form = StudentForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			group = form.cleaned_data['group_number']
			stid = form.cleaned_data['stid']
			if request.POST.get('Cancel','') == 'Cancel':
				return HttpResponseRedirect('/')
			if request.POST.get('Add','') == 'Add':
				st = Student.objects.create(name = name, email = email, group_number = group)
			if request.POST.get('Save','') == 'Save':
				ss = Student(id=stid, name = name, email = email, group_number = group)
				st = ss.save()
			if request.POST.get('Delete','') == 'Delete':
				ss = Student(id=stid, name = name, email = email, group_number = group)
				st = ss.delete()

			return HttpResponseRedirect('/')
		else:
			editadd=request.POST.get('Add',request.POST.get('Save',request.POST.get('Delete','')))
	return render(request, 'addstud.html', {'form': form, 'submit': editadd})

def AddScore(request):
	form = AddScoreForm()
	if request.method == 'GET':
		stid = request.GET.get('stud', 0)
		sid = request.GET.get('subj', 0)
		stud_id = Student.objects.filter(id = stid)
		subj_id = Subject.objects.filter(id = sid)

		score = '-'
		editadd = 'Add'
		if sid != 0 and stid!=0:
			s = Score.objects.filter(stud_id=stid, subj_id=sid)
			if s.exists():
				stud_id = stud_id[0].name
				subj_id = subj_id[0].sub_name
				score = s[0].score
				print(score)
				editadd = 'Save'
				form = AddScoreForm(initial={'score' : score, 'sid':sid,'stid':stid, 'stud_id' : stud_id, 'subj_id' : subj_id })
			else:
				stud_id = stud_id[0].name
				subj_id = subj_id[0].sub_name
				editadd = 'Add'
				form = AddScoreForm(initial={'score' : 0, 'sid':sid,'stid':stid, 'stud_id' : stud_id, 'subj_id' : subj_id })
		

	else:
		form = AddScoreForm(request.POST)
		if form.is_valid():
			score = form.cleaned_data['score']
			stud_id = form.cleaned_data['stud_id']
			subj_id = form.cleaned_data['subj_id']
			sid = form.cleaned_data['sid']
			stid = form.cleaned_data['stid']
			stud = Student.objects.filter(id = stid)
			subj = Subject.objects.filter(id = sid)
			if request.POST.get('Cancel','') == 'Cancel':
				return HttpResponseRedirect('/')
			if request.POST.get('Add','') == 'Add':
				st = Score.objects.create(stud_id=stud[0], subj_id=subj[0], score = score)
			if request.POST.get('Save','') == 'Save':
				sc = Score.objects.filter(stud_id=stud[0], subj_id=subj[0])
				sc0 = sc[0]
				sc0.score = score
				st = sc0.save()
			if request.POST.get('Delete','') == 'Delete':
				sc = Score.objects.filter(stud_id=stud[0], subj_id=subj[0])
				sc0 = sc[0]
				st = sc0.delete()
			return HttpResponseRedirect('/')
		else:
			editadd=request.POST.get('Add',request.POST.get('Save',request.POST.get('Delete','')))

			return render(request, 'addscore.html', {'form': form, 'submit': editadd, 'error': 'Неврные данные'})	
	return render(request, 'addscore.html', {'form': form, 'submit': editadd})


class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		
		STAT = Statistics
		context.update(
			{
				'students_statistics': STAT.GetList(),
				'subjects': STAT.GetListSubj
			}
		)
		return context



class Statistics:
	

	def GetList():
		spisok = []
		st = Student.objects.all().order_by('id')
		for s in st:
			studs = {'id': s.id,'name' : s.name, 'email' :s.email,'group_number' : s.group_number, 'scores'  : []}
			for subj in Statistics.GetListSubj():
				sc=Score.objects.filter(subj_id = subj['id'], stud_id = s.id)
				if sc.exists():
					studs['scores'].append({'score':sc[0].score,'id':subj['id']})  
				else:
					studs['scores'].append({'score':'-','id':subj['id']})
			spisok.append(studs)

		return spisok
	def GetListSubj():
		spisok = []
		ss = Subject.objects.all()
		for s in ss:
			spisok.append({'id':s.id,'name':s.sub_name, 'hours':s.sub_hours})
		return spisok	



