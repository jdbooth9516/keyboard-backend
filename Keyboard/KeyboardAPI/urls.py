from django.urls import path 
from . import views 


urlpatterns = [
    path("users/", views.User_list.as_view()),
    path("PaymentAccount/", views.Payment_account_list.as_view()),
    path("PaymentAccount/<int:User_id>/", views.Payment_account_list.as_view()),
    path("layouts/", views.Layout_List.as_view()),
]
