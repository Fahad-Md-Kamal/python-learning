from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from basket.basket import Basket
from store.models import Product


def basket_summery(request):
    """
    Basket's Final summary presenter
    """
    basket = Basket(request)
    context = {'basket': basket}
    return render(request, 'store/basket/summary.html', context)


def basket_add(request):
    """
    Add product to the basket
    """
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        # Count the Items of the basket.
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})

        return response


def basket_delete(request):
    """
    Delete product from the basket
    """
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        # Count the Items of the basket.
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})

        return response


def basket_update(request):
    """
    Update product of the basket
    """
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})

        return response
