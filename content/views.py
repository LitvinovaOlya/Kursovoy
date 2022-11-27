from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from content.forms import *
from django.db.models import F


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ZayavkiForm(request.POST)
        name = request.POST['name_klient']
        vizajist_id = request.POST['vizajist']
        pricheska_id = request.POST['pricheski']
        makeup_id = request.POST['makeup']
        vizajist_kvalification = Vizajisti.objects.get(pk=vizajist_id).kvalifikaciya_id
        procent = Kvalifikaciya.objects.get(pk=vizajist_kvalification).procent
        if pricheska_id:
            pricheska_stoimost = Pricheski.objects.get(pk=pricheska_id).stoimost
            stoimost = pricheska_stoimost + procent
        elif makeup_id:
            makeup_stoimost = Pricheski.objects.get(pk=makeup_id).stoimost
            stoimost = makeup_stoimost + procent
        elif pricheska_id and makeup_id:
            pricheska_stoimost = Pricheski.objects.get(pk=pricheska_id).stoimost
            makeup_stoimost = Pricheski.objects.get(pk=makeup_id).stoimost
            stoimost = pricheska_stoimost + procent + makeup_stoimost + procent
        else:
            return render(request, 'error.html', {'form': form})
        if form.is_valid():
            form.save()
            return render(request, 'spasibo.html', {'form': form, "stoimost": stoimost, "name": name})
    else:
        form = ZayavkiForm()
    return render(request, 'index.html', {'form': form, 'title': 'О нас'})


def service(request):
    form = ZayavkiForm()
    kvalifikaciya = Kvalifikaciya.objects.all()
    pricheski = Pricheski.objects.all()
    makeup = Makeup.objects.all()
    stoimost = []
    for i in makeup:
        for j in kvalifikaciya:
            stoimost.append(j.procent * i.stoimost)

    return render(request, 'service.html',
                  {'title': 'Услуги', "form": form, "kvalifikaciya": kvalifikaciya, "pricheski": pricheski,
                   "makeup": makeup, "stoimost": stoimost})


def about_us(request):
    form = ZayavkiForm()
    vizajist = Vizajisti.objects.all()
    return render(request, 'about_us.html', {'title': 'О нас', "form": form, 'vizajist': vizajist})


def contact(request):
    form = ZayavkiForm()
    return render(request, 'contact.html', {'title': 'Контакты', "form": form})


@login_required
def adminka(request):
    zayavki = Zayavki.objects.all()
    return render(request, 'adminka.html', {'zayavki': zayavki, 'title': "Панель управления"})


@login_required
def delete_zayavka(request, id_zayavka):
    zayavka = Zayavki.objects.get(pk=id_zayavka)
    zayavka.delete()
    return redirect('adminka')


@login_required
def update_zayavka(request, id_zayavka):
    zayavka = Zayavki.objects.get(pk=id_zayavka)
    form = ZayavkiForm(request.POST or None, instance=zayavka)
    if form.is_valid():
        form.save()
        return redirect('adminka')
    return render(request, 'update_zayavka.html', {'zayavka': zayavka, 'form': form})


@login_required
def admin_vizajist(request):
    vizajist = Vizajisti.objects.all()
    return render(request, 'admin_vizajist.html', {'vizajist': vizajist, 'title': "Панель управления"})


@login_required
def delete_vizajist(request, id_vizajist):
    vizajist = Vizajisti.objects.get(pk=id_vizajist)
    vizajist.delete()
    return redirect('admin_vizajist')


@login_required
def update_vizajist(request, id_vizajist):
    vizajist = Vizajisti.objects.get(pk=id_vizajist)
    form = VizajisForm(request.POST or None, request.FILES or None, instance=vizajist)
    if form.is_valid():
        form.save()
        return redirect('admin_vizajist')
    return render(request, 'update_vizajist.html', {'vizajist': vizajist, 'form': form})


@login_required
def add_vizajist(request):
    form = VizajisForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_vizajist')
    return render(request, 'add_vizajist.html', {'form': form})


@login_required
def admin_makeup(request):
    makeup = Makeup.objects.all()
    return render(request, 'admin_makeup.html', {'makeup': makeup, 'title': "Панель управления"})


@login_required
def delete_makeup(request, id_makeup):
    makeup = Makeup.objects.get(pk=id_makeup)
    makeup.delete()
    return redirect('admin_makeup')


@login_required
def update_makeup(request, id_makeup):
    makeup = Makeup.objects.get(pk=id_makeup)
    form = MakeupForm(request.POST or None, request.FILES or None, instance=makeup)
    if form.is_valid():
        form.save()
        return redirect('admin_makeup')
    return render(request, 'update_makeup.html', {'makeup': makeup, 'form': form})


@login_required
def add_makeup(request):
    form = MakeupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_makeup')
    return render(request, 'add_makeup.html', {'form': form})


@login_required
def admin_pricheski(request):
    pricheski = Pricheski.objects.all()
    return render(request, 'admin_pricheski.html', {'pricheski': pricheski, 'title': "Панель управления"})


@login_required
def delete_pricheski(request, id_pricheski):
    pricheski = Pricheski.objects.get(pk=id_pricheski)
    pricheski.delete()
    return redirect('admin_pricheski')


@login_required
def update_pricheski(request, id_pricheski):
    pricheski = Pricheski.objects.get(pk=id_pricheski)
    form = PricheskiForm(request.POST or None, request.FILES or None, instance=pricheski)
    if form.is_valid():
        form.save()
        return redirect('admin_pricheski')
    return render(request, 'update_pricheski.html', {'pricheski': pricheski, 'form': form})


@login_required
def add_pricheski(request):
    form = PricheskiForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_pricheski')
    return render(request, 'add_pricheski.html', {'form': form})


@login_required
def admin_kvalif(request):
    kvalif = Kvalifikaciya.objects.all()
    return render(request, 'admin_kvalif.html', {'kvalif': kvalif, 'title': "Панель управления"})


@login_required
def delete_kvalif(request, id_kvalif):
    kvalif = Kvalifikaciya.objects.get(pk=id_kvalif)
    kvalif.delete()
    return redirect('admin_kvalif')


@login_required
def update_kvalif(request, id_kvalif):
    kvalif = Kvalifikaciya.objects.get(pk=id_kvalif)
    form = KvalifikaciyaForm(request.POST or None, instance=kvalif)
    if form.is_valid():
        form.save()
        return redirect('admin_kvalif')
    return render(request, 'update_kvalif.html', {'kvalif': kvalif, 'form': form})


@login_required
def add_kvalif(request):
    form = KvalifikaciyaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_kvalif')
    return render(request, 'add_kvalif.html', {'form': form})
