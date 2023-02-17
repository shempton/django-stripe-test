from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Item
import stripe


stripe.api_key = 'sk_test_51McOfxGz3xAUiJZ3gXuNcEJgeUCTqRwHGl6YxaaaS817gfTGsGDh0hWioJEg9xVfIAIQLmzY1cbGlBZ6AdUVCYMR00hIaQYafe'


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item/index.html', {'item': item})


def create_checkout_session(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    session = stripe.checkout.Session.create(        
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount_decimal': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )
    return JsonResponse({'id': session.id})
