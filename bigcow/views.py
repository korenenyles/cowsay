from django.shortcuts import render
from bigcow.models import CowInput

# Create your views here.
def index(request):
    cow_data = CowInput.objects.all()
    return render(request, 'index.html', {'cow_data': cow_data})