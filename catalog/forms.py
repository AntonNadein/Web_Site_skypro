from django import forms

from .models import Product


class AddProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Выбирете категорию"

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price", "updated_at"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "description": forms.Textarea(attrs={"cols": 80, "rows": 10}),
        }
