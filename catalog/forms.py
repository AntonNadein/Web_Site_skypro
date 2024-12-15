import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class MixinProduct:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class AddProductForm(MixinProduct, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Выбирете категорию"

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "image",
            "category",
            "price",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "description": forms.Textarea(attrs={"cols": 80, "rows": 10}),
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            valid_formats = ["image/jpeg", "image/png"]
            if hasattr(image, "content_type"):
                if image.content_type not in valid_formats:
                    raise ValidationError("Неверный формат файла. Допустимые форматы: JPEG, PNG.")

            size = image.size
            if size > 1024 * 1024 * 70:
                raise ValidationError("Размер файла превышает 5Мб")
            return image

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        if self.validation_product(name):
            raise ValidationError("В названии продукта присутствуют недопустимые слова")
        elif self.validation_product(description):
            raise ValidationError("В описании продукта присутствуют недопустимые слова")
        else:
            return cleaned_data

    def validation_product(self, name):
        list_exeption = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        list_name = re.split(";|,| ", name)
        for item in list_name:
            if item.lower() in list_exeption:
                return True
        return False
