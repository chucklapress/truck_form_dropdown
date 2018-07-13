from django.shortcuts import render
from django.views.generic import TemplateView,View,CreateView,ListView
from django.http import HttpResponseRedirect
from django import forms
from app.models import VendorListing, Lala
from django.core.urlresolvers import reverse, reverse_lazy
from app.forms import VendorListingForm, LalaForm


def addLala(request):
    if request.method == 'GET':
        form = LalaForm()
        return render (request, 'form.html', {'form':form})
    elif request.method == 'POST':
        form = LalaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/hurray')
        else:
            return HttpResponseRedirect('/')




class VendorListingCreateView(CreateView):
    model = VendorListing
    fields = ['dateServing','Name', 'location','Address','zipCode','beginning', 'ending','city', 'userlocation']
    success_url = '/vendor_list'

class VendorListView(ListView):
    model = VendorListing

class HurrayView(TemplateView):
    template_name = 'congrats.html'
