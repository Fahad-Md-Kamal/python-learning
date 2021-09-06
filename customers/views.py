from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from products.utils import get_image


from .models import Customer

@login_required
def customer_corr_view(request):
    df = pd.DataFrame(Customer.objects.all().values())
    corr = round(df['budget'].corr(df['employment']), 2)

    plt.switch_backend('AGG')
    sns.jointplot(x='budget', y = 'employment', kind='reg', data=df).set_axis_labels('Company Budget', 'No of Employees')
    graph = get_image()

    context = {
        'graph': graph,
        'corr': corr,
    }

    return render(request, 'customers/main.html', context)