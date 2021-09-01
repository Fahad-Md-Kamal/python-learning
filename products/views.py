from django.shortcuts import render
from products.models import Product, Purchase
import pandas as pd

####### Time 1.06.15

def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values_list())
    context = {
        'products': product_df.to_html(),
        'purchase': purchase_df.to_html()
    }
    return render(request, 'products/main.html', context)

