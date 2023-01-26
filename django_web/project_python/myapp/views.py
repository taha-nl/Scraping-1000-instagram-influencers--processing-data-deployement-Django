from django.shortcuts import render
import pandas as pd
import json
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def table(request):
    df=pd.read_csv("C:/Users/user/Desktop/pweb/django_web/project_python/myapp/templates/instagram_scrapping.csv")
    df.dropna(inplace=True)
    # parsing the DataFrame in json format.
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    
    page = request.GET.get('page', 1)

    paginator = Paginator(data, 90)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {'d': data}
    return render(request,"table.html",context)

def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")

    
def contact(request):
    return render(request,"contact.html")

'''from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")



def home(request):
    return HttpResponse('Home page')

def room(request):
    return HttpResponse('Room page')'''