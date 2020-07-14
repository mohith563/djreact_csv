from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponse

# Create your views here.

from .forms import ProductForm

class DataView(FormView):
    form_class = ProductForm
    template_name = 'base.html'
    success_url = '/'

    def form_valid(self, form):
        form.process_data()
        return super().form_valid(form)




