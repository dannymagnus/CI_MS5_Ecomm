"""
A module for the bag context manager
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
# Internal
from products.models import Inventory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def bag_contents(request):
    """
    A context that contains the bag contents
    Args:
        request (object): HTTP request object.
    Returns:
        The bag contents context
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for sku, quantity in bag.items():
        inventory = get_object_or_404(Inventory, sku=sku)
        subtotal = inventory.product.price * quantity
        total += quantity * inventory.product.price
        print(total)
        product_count += quantity
        bag_items.append({
            'quantity': quantity,
            'inventory': inventory,
            'subtotal': subtotal,
        })

    # Delivery variables courtesy of Code Institute Boutique Ado
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context