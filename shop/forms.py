from .models import Category, Subcategory, Product
from django import forms

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.none())

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.all()


