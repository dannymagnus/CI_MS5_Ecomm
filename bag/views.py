from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Inventory, Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, slug):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')
    sku = request.POST.get('sku')
    item = get_object_or_404(Inventory, sku=sku)
    name = item.product.friendly_name
    product = get_object_or_404(Product, slug=slug)

    if sku in list(bag.keys()):
        bag[sku] += quantity
        messages.success(request, f'Added {item.product.friendly_name} to your bag')

    else:
        bag[sku] = quantity        
        messages.success(request, f'Added {item.product.friendly_name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


# def adjust_bag(request, item_id):
#     """Adjust the quantity of the specified product to the specified amount"""

#     quantity = int(request.POST.get('quantity'))
#     size = None
#     if 'product_size' in request.POST:
#         size = request.POST['product_size']
#         sku = request.POST['sku']
#     bag = request.session.get('bag', {})

#     if size:
#         if quantity > 0:
#             bag[item_id]['items_by_size'][size] = quantity
#             bag[item_id]['items_by_sku'][]
#         else:
#             del bag[item_id]['items_by_size'][size]
#             if not bag[item_id]['items_by_size']:
#                 bag.pop(item_id)
#     else:
#         if quantity > 0:
#             bag[item_id] = quantity
#         else:
#             bag.pop(item_id)

#     request.session['bag'] = bag
#     return redirect(reverse('view_bag'))


# def remove_from_bag(request, item_id):
#     """Remove the item from the shopping bag"""

#     try:
#         size = None
#         if 'product_size' in request.POST:
#             size = request.POST['product_size']
#         bag = request.session.get('bag', {})

#         if size:
#             del bag[item_id]['items_by_size'][size]
#             if not bag[item_id]['items_by_size']:
#                 bag.pop(item_id)
#         else:
#             bag.pop(item_id)

#         request.session['bag'] = bag
#         return HttpResponse(status=200)

#     except Exception as e:
#         return HttpResponse(status=500)