from django.shortcuts import render
from app.models.family_members import FamilyMembers
from django.http import HttpResponse
from django.template import loader

def members(request):
    family_members= [
        {"name":"Lando", "surname":"Norris", "age":"23", "born_date":"1999-12-10"},
        {"name":"daniel", "surname":"Norris", "age":"23", "born_date":"1999-12-10"},
        {"name":"ceci", "surname":"Norris", "age":"23", "born_date":"1999-12-10"}
    ]
    template = loader.get_template("templates_family.html") 
    return HttpResponse(template.render({"family": family_members}))
