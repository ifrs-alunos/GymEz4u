from django.db import models
from . import Gym
from portifolio.models import Plan

class Schedule(models.Model):
	nome = models.CharField(max_length=25)
	segunda_e = models.TimeField()
	segunda_s = models.TimeField()
	terca_e = models.TimeField()
	terca_s = models.TimeField()
	quarta_e = models.TimeField()
	quarta_s = models.TimeField()
	quinta_e = models.TimeField()
	quinta_s = models.TimeField()
	sexta_e = models.TimeField()
	sexta_s = models.TimeField()
	sabado_e = models.TimeField()
	sabado_s = models.TimeField()
	domingo_e = models.TimeField()
	domingo_s = models.TimeField()
	academia = models.ForeignKey(Gym, related_name="horarios", on_delete=models.CASCADE)
	planos = models.ForeignKey(Plan, related_name="horarios", on_delete=models.CASCADE)

	def __str__(self):
		retorno = {'segunda':[segunda_e,segunda_s], 'terca':[terca_e,terca_s], 'quarta':[quarta_e,quarta_s], 'quinta':[quinta_e,quinta_s], 'sexta':[sexta_e,sexta_s], 'sabado':[sabado_e,sabado_s], 'domingo':[domingo_e,domingo_s], }
		return retorno
