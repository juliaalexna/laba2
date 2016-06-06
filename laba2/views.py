# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from jul.models import Student, Subject, Score


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
		
pass



