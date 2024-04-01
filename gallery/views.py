from django.shortcuts import render, redirect

# Create your views here.
from .forms import PhotoForm
from .models import Photo


def gallery(request):
    photos = Photo.objects.all()
    return render(request, "gallery/index.html", {"photos": photos})


def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    form = PhotoForm()
    return render(request, "gallery/upload.html", {"form": form})
