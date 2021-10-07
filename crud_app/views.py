from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib import messages

from crud_app import models
from . import forms


class HomepageView(TemplateView):
    message = 'Astagfirullahil Azim'
    template_name = 'crud_app/home.html'


def category_create_view(request):
    template_name = 'crud_app/category-form.html'
    form = forms.CategoryForm()

    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            categ = category_form.save(commit=False)
            categ.created_by = request.user
            categ.save()
            messages.success(request, f'Category "{categ.name}" created successfully.')
        else:
            form = forms.CategoryForm(request.POST)
            messages.error(request, 'Form data is not valid')

    context = {
        'form': form,
    }
    return render(request, template_name, context)


# class CategoryCreateView(CreateView):
#     template_name = 'crud_app/category-form.html'
#     form_class = forms.CategoryForm

#     def post(self, request, *args, **kwargs):
#         category_form = forms.CategoryForm(request.POST)
#         if category_form.is_valid():
#             categ = category_form.save(commit=False)
#             categ.created_by = request.user
#             categ.save()
#             messages.success(request, f'Category {categ.name} created successfully.')
#         return super().post(request, *args, **kwargs)

# category_create_view = CategoryCreateView.as_view()

