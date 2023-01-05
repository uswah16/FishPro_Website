from django.shortcuts import render, redirect
from .models import *
from produksi_app.forms import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
from .forms import CreateUserForm

def halamansatu(request):
    ikan = Perikanan.objects.all()
    judul = "halamansatu"
    data = {
        "title" : judul,
        "heading" : judul,
        'ikan' : ikan,
    }
    return render(request, 'halamansatu.html', data)

def halamandua(request):
    ikan = Perikanan.objects.all()
    judul = "halamandua"
    data = {
        "title" : judul,
        "heading" : judul,
        'ikan' : ikan,
    }
    return render(request, 'halamandua.html', data)

def halamantiga(request):
    judul = "Halaman tiga"
    data = {
       "title" : judul,
       "heading" : judul,
    }
    return render(request, 'halamantiga.html', data)

def halamanempat(request):
    judul =  "halaman empat"
    data = {
       "title" : judul,
       "heading" : judul,
    }
    return render(request, 'halamanempat.html', data)

def tambah_data(request):
    if request.POST:
        form = FormPerikanan(request.POST)
        if form.is_valid():
            form.save()
            form = FormPerikanan()
            judul = "Tambah Data Perikanan"
            data={
                "title" : judul,
                "heading" : judul,
                "form" : form,
               "pesan" : "Data Perikanan Berhasil Ditambahkan",
            }
            return render(request, 'tambah_data.html', data)
    else:
        form = FormPerikanan()
        judul = "Tambah Data Perikanan"
        data={
            "title" : judul,
            "heading" : judul,
            "form" : form,
        }
        return render(request, 'tambah_data.html', data)

def update_data(request, id_ikan):
    ikan = Perikanan.objects.get(id = id_ikan)
    judul = "Update Data Perikanan"
    template = "update_data.html"
    if request.POST:
        form = FormPerikanan(request.POST, instance=ikan)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate"
            data = {
                "title" : judul,
                "heading" : judul,
                "pesan" : pesan,
                "form" : form,
                "ikan" : ikan
            }
        return render(request, template, data)

    else:
        form = FormPerikanan(instance=ikan)
        data = {
        "title" : judul,
        "heading" : judul,
        "form" : form,
        "ikan" : ikan
        }
        return render(request, template, data)

def delete_data(request, id_ikan):
    ikan = Perikanan.objects.get(id = id_ikan)
    ikan.delete()
    return redirect('/halamansatu/')

def data1(request):
    judul =  "data"
    data = {
        "title" : judul,
        "heading" : judul,
    }
    return render(request, 'data1.html', data)

def landing(request):
    judul =  "halaman landing"
    data = {
       "title" : judul,
       "heading" : judul,
    }
    return render(request, 'landing.html', data)

def loginPage(request):
    
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/halamansatu/')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')