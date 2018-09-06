from django.db import models

# Create your models here.



class Horarios(models.Model):

	nomeHorario = models.CharField(max_length=20)

	horarioInicio = models.CharField(max_length=20)



class Refeicao(models.Model):

	arroz = models.CharField(max_length=20)
	feijao = models.CharField(max_length=20)

	guarnicao = models.CharField(max_length=40)

	proteina = models.CharField(max_length=20)
	proteina2 = models.CharField(max_length=20)
	opcaoVegetariana = models.CharField(max_length=20)

	salada = models.CharField(max_length=20)

	sobremesa = models.CharField(max_length=20)

	suco = models.CharField(max_length=20)


	data = models.DateField('dataRefeicao', auto_now_add = False)
	diaDaSemana = models.CharField(max_length=20)

	horario = models.OneToOneField(Horarios, on_delete=models.CASCADE, null=True)

	aviso = models.CharField(max_length=140)

