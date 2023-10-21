from django.shortcuts import render
from .models import *
from .forms import RecordForm

def index(request):
    product = Products.objects.all()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm()
        
    context = {'product': product, 'form': form}  # Объедините переменные в один словарь
    return render(request, 'main/index.html', context)  # Переда словарь context в качестве контекста

