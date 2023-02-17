from django.urls import path

from . import views


urlpatterns = [
    path('item/<int:item_id>/', views.detail, name='detail'),
    path('buy/<int:item_id>/', views.create_checkout_session, name='get_session_id'),
]