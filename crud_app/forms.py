from django import forms
from django import forms
from django.forms import fields, widgets
from .models import Category, Product


class AddCategoryForm(forms.ModelForm):
    name = forms.CharField(label='Category')

    class Meta:
        model = Category
        fields =  ['name', 'short_description', 'parent_category']

    
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        category = Category.objects.filter(name=name)
        if len(category) > 0:
            raise forms.ValidationError(f'Category "{name}" Already Exists')
        return name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder': 'Category Name'}
        )
        self.fields['short_description'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder': 'Write short description within 300 words.'}
        )

class UpdateCategoryForm(forms.ModelForm):
    name = forms.CharField(label='Category')

    class Meta:
        model = Category
        fields =  ['name', 'short_description', 'parent_category']
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder': 'Category Name'}
        )
        self.fields['short_description'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder': 'Write short description within 300 words.'}
        )

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name','price', 'description', 'category','is_available', 'images']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['images'].widget.attrs.update(
            {'class':'form-control mb-3', 'multiple':'multiple'}
        )