from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from .models import Refeicao


def index(request):

    latestRefeicao = Refeicao.objects.order_by('data')[:1]
    context = { 'latestRefeicao': latestRefeicao[0] }

    return render(request, 'bandejao/index.html', context)


def detail(request, refeicaoID):
    return HttpResponse("Aqui %s ." % refeicaoID)
