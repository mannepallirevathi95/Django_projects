from socket import fromshare
from typing import ItemsView
from django import forms
from .models import Item

# create class to add items that inheret from modelform
# creating a meta class holding info of that form (i.e., what should be presented)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_discrip', 'item_image', 'item_price']
