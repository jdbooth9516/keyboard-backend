from django.urls import path 
from . import views 


urlpatterns = [
    path("users/", views.User_list.as_view()),
    path("login/", views.Login.as_view()),
    path("PaymentAccount/", views.Payment_account_list.as_view()),
    path("PaymentAccount/<int:User_id>/", views.Payment_account_list.as_view()),
    path("layouts/", views.Layout_List.as_view()),
    path("services/", views.Services_list.as_view()),
    path("extras/", views.Extras_list.as_view()),
    path("switches/", views.Switches_list.as_view()),
    path("build/", views.Build_list.as_view()),
    path("cart/", views.Shopping_cart_list.as_view()),
    path("cart/<int:User_id>/", views.Shopping_cart_list.as_view()),
    path("payment/", views.Payment.as_view()),
    path("orders/", views.Orders.as_view())
]
