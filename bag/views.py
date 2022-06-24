"""
A module for bag app views
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports
# 3rd Party
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse
from django.contrib import messages
# Internal
from products.models import Inventory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def view_bag(request):
    """
    A view that renders the bag contents page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, slug):
    """
    Add a quantity of the specified product to the shopping bag
    """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    # redirect url credit Code Institute Boutique Ado Project
    redirect_url = request.POST.get('redirect_url')
    sku = request.POST.get('sku')
    item = get_object_or_404(Inventory, sku=sku)

    if sku in list(bag.keys()):
        bag[sku] += quantity
        messages.success(
            request, f'Added {item.product.friendly_name} to your bag'
            )

    else:
        bag[sku] = quantity
        messages.success(
            request, f'Added {item.product.friendly_name} to your bag'
            )

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, inventory_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    item = get_object_or_404(Inventory, pk=inventory_id)
    sku = item.sku

    if quantity > 0:
        bag[sku] = quantity

    else:
        messages.success(
            request, f'Removed {item.product.friendly_name} from your bag'
            )
        bag.pop(sku)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, inventory_id):
    """
    Remove the item from the shopping bag
    """
    try:
        bag = request.session.get('bag', {})
        item = get_object_or_404(Inventory, pk=inventory_id)
        sku = item.sku

        bag.pop(sku)
        messages.success(
            request, f'Removed {item.product.friendly_name} from your bag'
            )

        return redirect(reverse('view_bag'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
