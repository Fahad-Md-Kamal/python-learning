from django.shortcuts import render
from products.models import Product, Purchase
import pandas as pd

from .utils import get_simple_plot
from .forms import PurchaseForm

# time 2.41.12


def chart_select_view(request):
    graph = None
    error_message = None
    df = None
    price = None

    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    product_df['product_id'] = product_df['id']

    if purchase_df.shape[0] > 0:
        df = pd.merge(purchase_df, product_df, on='product_id')\
            .drop(['id_y', 'date_y'], axis=1)\
            .rename({'id_x': 'id', 'date_x': 'date'}, axis=1)
        price = df['price']

        if request.method == 'POST':
            chart_type = request.POST['sales']
            date_form = request.POST['date_from']
            date_to = request.POST['date_to']

            print(chart_type)

            df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')

            if chart_type != "":
                if date_form != "" and date_to != "":
                    df = df[(df['date'] > date_form) & (df['date'] < date_to)]
                    df2 = df.groupby('date', as_index=False)[
                        'total_price'].agg('sum')

                graph = get_simple_plot(
                    chart_type, x=df2['date'], y=df2['total_price'], data=df)

            else:
                error_message = 'Please select a chart type to continue'

    else:
        error_message = 'No records in the database'

    context = {
        'price': price,
        'error_message': error_message,
        'graph': graph,
    }
    return render(request, 'products/main.html', context)


def add_purchase_view(request):
    form = PurchaseForm(request.POST or None)
    added_message = None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.salesman = request.user
        obj.save()

        form = PurchaseForm()
        added_message = "The purchase has been added"

    context = {
        'form': form,
        'added_message': added_message,
    }
    return render(request, 'products/add.html', context)
