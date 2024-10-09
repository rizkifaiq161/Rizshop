from django.forms import ModelForm
from main.models import Item
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "description", "amount"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        # Bersihkan dari tag HTML jika ada
        return strip_tags(name)
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        # Pastikan nilai price adalah angka positif
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
    
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        # Pastikan jumlah adalah angka positif
        if amount < 1:
            raise forms.ValidationError("Amount must be at least 1.")
        return amount
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        # Bersihkan dari tag HTML jika ada
        return strip_tags(description)
