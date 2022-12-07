from django.shortcuts import render
from app.models.family_members import FamilyMembers
from django.http import HttpResponse
from django.template import loader

def members(request):
    family_members= [
        {"name":"Lando", "surname":"Norris", "age":"23", "born_date":"1999-11-13"},
        {"name":"Daniel", "surname":"Ricciardo", "age":"33", "born_date":"1989-07-01"},
        {"name":"Lewis", "surname":"Hamilton", "age":"37", "born_date":"1985-01-07"}
    ]
    template = loader.get_template("templates_family.html") 
    return HttpResponse(template.render({"family": family_members}))
