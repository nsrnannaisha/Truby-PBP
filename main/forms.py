from django.forms import ModelForm
from main.models import productEntry
from django.utils.html import strip_tags

class productEntryForm(ModelForm):
    class Meta:
        model = productEntry
        fields = ["product", "price", "description", "rating", "quantity"]

    def clean_product(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        return strip_tags(rating)
    
    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        return strip_tags(quantity)