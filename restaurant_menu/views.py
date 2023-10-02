from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE
# Create your views here.

class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")

    # render the html page using the one line code below
    template_name = "index.html"

    # must name this method exactly like this: this method will display content on the html page
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE

        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
