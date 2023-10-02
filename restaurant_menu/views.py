from django.shortcuts import render
from django.views import generic
from .models import Item
# Create your views here.

class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")

    # render the html page using the one line code below
    template_name = "index.html"

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
