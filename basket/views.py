from django.shortcuts import render


def basket_summery(request):
    return render(request, 'store/basket/summary.html', {})
