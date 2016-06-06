from django.apps import AppConfig
from laba2 import models

class JulConfig(AppConfig):
 	name = 'jul'
 	# def ready(self):
 	# 	Student = self.get_model('Student')
 	# 	Student.objects.create(id = 5, name = 'D', email = 'mrv@security.tomsk.ru', group_number = 724)
 		# 	Subject = self.get_model('Subject')
 	# 	Score = self.get_model('Score')
 	# 	Student.objects.all().delete()
 	# 	Subject.objects.all().delete()

 	# 	st = [Student.objects.create(id = 1, name = 'Романов', email = 'rom@security.tomsk.ru', group_number = 724),
		# Student.objects.create(id = 2, name = 'Клочков', email = 'lol@mail.ru', group_number = 734), 
		# Student.objects.create(id = 3, name = 'Лысак', email = 'liy@mail.ru', group_number = 724),
		# ss = [Subject.objects.create(id = 1, sub_name = 'Философия', sub_hours = 42),
		# Subject.objects.create(id = 2, sub_name = 'Матанализ', sub_hours = 26),		
		# Subject.objects.create(id = 3, sub_name = 'ТиМП', sub_hours = 108)]
		
# 		# Score.objects.create(id = 1, subj_id = 1, score = 5)
