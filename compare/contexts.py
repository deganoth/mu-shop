from django.shortcuts import get_object_or_404
from products.models import Product


def compare_contents(request):
    """
    Esures cart contents are available to
    view on any page within our collection of apps.
    """
    compare = request.session.get('compare', {})

    compare_items = []
    compare_count = 0

    for id, quantity in compare.items():
        product = get_object_or_404(Product, pk=id)
        compare_count += quantity
        compare_items.append(
            {'id': id, 'quantity': quantity, 'product': product}
            )

    return {'compare_items': compare_items, 'compare_count': compare_count}
