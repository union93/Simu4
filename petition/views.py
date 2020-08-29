from django.shortcuts import render, redirect
from .models import Petition
from .forms import PetitionForm
from accounts.models import User


def index(request):
    return render(request,'petition/home/home.html')

def petition_write(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            petition = Petition()
            petition.title = form.cleaned_data['title']
            petition.contents = form.cleaned_data['contents']
            petition.writer = user_id
            petition.save()
            return redirect('petition/petition_write.html')
    else:
        form = PetitionForm()
    return render(request, 'petition/petition_write.html', {'form': form})

def petition_list(request):
    petitions = Petition.objects.all().order_by('-id')
    return render(request, 'petition/petition_list.html')
    