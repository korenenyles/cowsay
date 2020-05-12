from django.shortcuts import render, reverse, HttpResponseRedirect
from bigcow.models import CowInput
from bigcow.forms import AddTextInput
import subprocess

  

def index(request):
    if request.method == "POST":
        form = AddTextInput(request.POST)
        if form.is_valid():
            cow_data = form.cleaned_data
            CowInput.objects.create(
                cow_input = cow_data['cow_input'] 
            )
            cowput = cow_words(cow_data['cow_input'])
            form = AddTextInput()
                     
            
            return render(request, 'index.html', {"form":form,  'cowput':cowput})
        form = AddTextInput()
    return render(request, 'index.html', {'form':form})

def cow_words(string):
    cow_output = subprocess.Popen(['cowsay', string], stdout=subprocess.PIPE).communicate()[0]
    return cow_output.decode("utf8")

