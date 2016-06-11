# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from jul.models import Student, Subject, Score
from laba2.forms import SubForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import QueryDict

def Addsubj(request):
	form = SubForm()
	if request.method == 'GET':
		sid=request.GET.get('subj',0)
		name = ''
		hours = 0
		editadd = 'Add'
		if sid != 0:
			s = Subject.objects.filter(id = sid)
			if s.exists():
				name = s[0].sub_name
				hours = s[0].sub_hours
				editadd = 'Edit'
		form = SubForm(initial={'subject' : name, 'hours': hours, 'sid':sid})
	else:
		form = SubForm(request.POST)
	if form.is_valid():
		subject = form.cleaned_data['subject']
		hours = form.cleaned_data['hours']
		sid = form.cleaned_data['sid']
		if request.POST.get('Add','') == 'Add':
			sub = Subject.objects.create(sub_name = subject, sub_hours = hours)
		if request.POST.get('Edit','') == 'Edit':
			ss=Subject(id=sid,sub_name = subject, sub_hours = hours)
			sub = ss.save()
		if request.POST.get('Delete','') == 'Delete':
			ss=Subject(id=sid,sub_name = subject, sub_hours = hours)
			sub = ss.delete()



		return HttpResponseRedirect('/')
	return render(request, 'addsubj.html', {'form': form, 'submit': editadd})


class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		
		STAT = Statistics
		context.update(
			{
				'students_statistics': STAT.GetList(),
				#'excellent_students': STAT.GetGood(),
				#'bad_students': STAT.GetBad()
				'subjects': STAT.GetListSubj
			}
		)
		return context



class Statistics:
	#def __init__(self,studentlist):
	#	self.studentlist = studentlist
	

	def GetList():
		spisok = []
		st = Student.objects.all()
		for s in st:
			studs = {'id': s.id,'name' : s.name, 'email' :s.email,'group_number' : s.group_number, 'scores'  : []}
			for subj in Statistics.GetListSubj():
				sc=Score.objects.filter(subj_id = subj['id'], stud_id = s.id)
				if sc.exists():
					studs['scores'].append(sc[0].score)  
				else:
					studs['scores'].append('-')
			spisok.append(studs)

		return spisok
	def GetListSubj():
		spisok = []
		ss = Subject.objects.all()
		for s in ss:
			spisok.append({'id':s.id,'name':s.sub_name, 'hours':s.sub_hours})
		return spisok	



