from django.forms import ModelForm
from .models import Game, Product

class ProductForm(forms.ModelForm):
    class Meta:
        fields = ("game", "price")
        model = Product
