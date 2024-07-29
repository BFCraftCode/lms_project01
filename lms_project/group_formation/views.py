from django.shortcuts import render
from .models import Apprenant, Groupe
import random

def index(request):
    if request.method == "POST":
        apprenants = request.POST.getlist('apprenants')
        nombre_groupes = int(request.POST['nombre_groupes'])

        # Suppression des groupes précédents
        Groupe.objects.all().delete()

        # Création des nouveaux apprenants
        apprenants_obj = [Apprenant.objects.create(nom=nom.split()[1], prenom=nom.split()[0]) for nom in apprenants]

        # Mélange des apprenants
        random.shuffle(apprenants_obj)

        # Formation des groupes
        groupes = [Groupe.objects.create(nom=f"Groupe {i+1}") for i in range(nombre_groupes)]
        for i, apprenant in enumerate(apprenants_obj):
            groupes[i % nombre_groupes].apprenants.add(apprenant)

        return render(request, 'group_formation/index.html', {'groupes': groupes})

    return render(request, 'group_formation/index.html', {'groupes': None})

