from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ScrapedView(TemplateView):
    template_name:str = "view_items/index.html"