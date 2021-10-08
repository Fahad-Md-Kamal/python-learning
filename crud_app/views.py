from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib import messages

from crud_app import models
from . import forms


# class HomepageView(TemplateView):
#     message = 'Astagfirullahil Azim'
#     template_name = 'crud_app/home.html'

# homepage_view = HomepageView.as_view()

def homepage_view(request):
    template_name = 'crud_app/home.html'
    products = models.Product.objects.all()
    context = {'products': products}
    return render(request, template_name, context)

def category_create_view(request):
    template_name = 'crud_app/category/category-form.html'
    form = forms.AddCategoryForm()
    if request.method == 'POST':
        category_form = forms.AddCategoryForm(request.POST)
        if category_form.is_valid():
            categ = category_form.save(commit=False)
            categ.created_by = request.user
            categ.save()
            messages.success(request, f'Category "{categ.name}" created successfully.')
        else:
            form = forms.AddCategoryForm(request.POST)
            messages.error(request, 'Form data is not valid')
    context = {'form': form, 'form_action': 'Add'  }
    return render(request, template_name, context)


def category_update_view(request, slug):
    template_name = 'crud_app/category/category-form.html'
    category_obj = get_object_or_404(models.Category, slug=slug)
    if request.method == "POST":
        form = forms.UpdateCategoryForm(request.POST or None, instance=category_obj)
        if form.is_valid():
            categ =  form.save(commit=False)
            categ.updated_by = request.user
            categ.save()
            return redirect('/')
    else:
        form = forms.UpdateCategoryForm(instance=category_obj)
    context = {'form':form, 'form_action': 'Update' }
    return render(request, template_name, context)


def add_product_view(request):
    template_name = 'crud_app/product/product-form.html'
    form = forms.ProductForm()
    if request.method == "POST":
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.created_by = request.user
            form.save()
            messages.success(request, f'Product "{prod.name}" added successfully.')
            return redirect(prod.get_absolute_url())
        else:
            form = forms.ProductForm(request.POST)
            messages.error(request, 'Form data is not valid')
    context ={ 'form' : form, 'form_action' : 'Add' }
    return render(request, template_name, context)


def update_product_view(request, slug):
    template_name = 'crud_app/product/product-form.html'
    form = forms.ProductForm()
    action = 'Update'
    product_obj = get_object_or_404(models.Product, slug=slug)
    if request.method == "POST":
        form = forms.ProductForm(request.POST or None, instance=product_obj)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.updated_by = request.user
            form.save()
            messages.success(request, f'Product "{prod.name}" updated successfully.')
            return redirect(prod.get_absolute_url())
    form = forms.ProductForm(instance=product_obj)
    context ={ 'form' : form, 'form_action' : action }
    return render(request, template_name, context)


def detail_product_view(request, slug):
    template_name = 'crud_app/product/detail-product.html'
    product = get_object_or_404(models.Product, slug=slug)
    context = { 'product': product }
    return render(request, template_name, context)

def delete_product_view(request, slug):
    models.Product.objects.delete(slug=slug)
