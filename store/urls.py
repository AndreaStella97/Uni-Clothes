from django.urls import path
from . import views
from. import api

urlpatterns = [
    path('', views.HomeView.as_view(), name="home_view"),
    path('clothing/', views.ItemsListView.as_view(), name="items_list_view"),
    path('api/items-list/', api.ItemsListApi.as_view(), name="items_list_api"),
    path('item/<slug:slug>', views.ItemDetailView.as_view(), name="item_detail_view"),
    path('api/items-in-stock/', api.ItemsInStockApi.as_view(), name="items_in_stock_api"),
    path('api/shopping-cart/', api.ShoppingCartApi.as_view(), name="shopping_cart_api"),
    path('shopping-cart/', views.ShoppingCartView.as_view(), name="shopping_cart_view"),
    path('api/order-item/', api.OrderItemApi.as_view(), name="order_item_api"),
    path('api/purchase/', api.PurchaseApi.as_view(), name="purchase_api"),
    path('api/one-shot/', api.OneShotApi.as_view(), name="one_shot_api"),

]