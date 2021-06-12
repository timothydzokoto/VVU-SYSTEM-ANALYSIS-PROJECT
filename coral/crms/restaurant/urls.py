from django.urls import path

from .views import (
    IndexPageView, 
    FoodListView,
    FoodOrderView,
    OrderConfirmation,
    OrderPayConfirmation,
    TableReservationView,
    ReservationConfirmationView,
    RecreationalActivityView,
    RecreationConfirmationView,
    DashboardView,
)


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('foods/', FoodListView.as_view(), name='food_list'),
    path('<int:pk>/order/', FoodOrderView.as_view(), name='food_order'),
    path('order_confirmation/<int:pk>/', OrderConfirmation.as_view(), name = 'order-confirmation' ),
    path('payment-confirmation/', OrderPayConfirmation.as_view(), name = 'payment-confirmation'),
    path('reservation/', TableReservationView.as_view(), name='reservation'),
    path('reservation_confirmation/<int:pk>/', ReservationConfirmationView.as_view(), name = 'reservation-confirmation'),
    path('recreation/', RecreationalActivityView.as_view(), name='recreation'),
    path('recreation_confirmation/<int:pk>/', RecreationConfirmationView.as_view(), name = 'recreation-confirmation' ),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]