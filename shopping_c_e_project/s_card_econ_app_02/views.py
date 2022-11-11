from django.shortcuts import render
from s_card_econ_app.models import product
from django.db.models import Q
# Create your views here.
def searchResult(request):
    Products= None
    query = None
    if 'q' in request.GET:
     query=request.GET.get('q')
     Products=product.objects.all().filter(Q(name__contains=query)  | Q(description__contains=query))

    return render(request,'search.html',{'query':query,'Products':Products})
