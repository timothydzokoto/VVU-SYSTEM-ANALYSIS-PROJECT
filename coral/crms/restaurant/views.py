import  json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin # new

from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
)
from django.views import View
from django.views.generic.edit import CreateView
from .models import (
    Food, 
    Order,
    Recreation,
    TableReservation,
    Reservation,
    Recreation,
    Activity,
)
from .forms import (
    RecreationForm,
    TableReservationForm,
)


# Create your views here.

class IndexPageView(ListView):
    template_name = 'restaurant/index.html'
    context_object_name = 'activities'
    model = Activity


class FoodListView(LoginRequiredMixin, ListView):
    template_name = 'food_list.html'
    context_object_name = 'foods'
    model = Food


class FoodOrderView(LoginRequiredMixin, View):
    template_name = 'restaurant/food_order.html'

    def get(self, request, pk, *args, **kwargs):
        my_food = Food.objects.get(pk=pk)
        print(my_food)
        context = {
            'my_food': my_food,
        }

        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        my_food = Food.objects.get(id=pk)
        quantity = int(request.POST.get('quantity'))
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')

        # calculate the purchase total
        price = quantity * my_food.price


        order = Order.objects.create(
            customer = request.user,
            food = my_food,
            quantity = quantity,
            price = price,
            email = email,
            street = street,
            city = city,
            state = state, 
            zip_code = zip_code,
        )

        context = {
            'order': order,
        }


        return redirect('order-confirmation', pk=order.pk)


class OrderConfirmation(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        context = {
            'pk': order.pk,
            'price': order.price,
            'quantity': order.quantity,
            'food': order.food,
        }

        return render(request, 'restaurant/order_confirmation.html', context)
        
    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)
        if data['isPaid']:
            order = Order.objects.get(pk=pk)
            order.is_paid = True
            order.save()
            
        return redirect('payment-confirmation')


class OrderPayConfirmation(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant/order_pay_confirmation.html')


class TableReservationView(LoginRequiredMixin, CreateView):
    model = TableReservation
    form_class = TableReservationForm
    template_name = 'restaurant/table_reservation.html'

class ReservationConfirmationView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        table_reservation = TableReservation.objects.get(id = pk)
        print(table_reservation.type.price)

        context = {
            'id': table_reservation.id,
            'type': table_reservation.type,
            'no_people': table_reservation.no_people,
            'phone': table_reservation.phone,
            'price': table_reservation.type.price,
            'customer': request.user,
        }

        return render(request, 'restaurant/reservation_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)
        if data['isPaid']:
            reservation = TableReservation.objects.get(id=pk)
            reservation.customer = request.user
            reservation.email = request.user.email
            reservation.price = float(data['price'])
            reservation.is_paid = True
            reservation.save()
            
        return redirect('payment-confirmation')


class RecreationalActivityView(LoginRequiredMixin, CreateView):
    model = Recreation
    form_class = RecreationForm
    template_name = 'restaurant/recreation.html'


class RecreationConfirmationView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        recreation = Recreation.objects.get(id = pk)
        total_price = recreation.activity.price * recreation.no_days
        context = {
            'id': recreation.id,
            'activity': recreation.activity,
            'no_people': recreation.no_days,
            'phone': recreation.phone,
            'price': recreation.activity.price,
            'total_price': total_price,
        }


        return render(request, 'restaurant/recreation_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)
        if data['isPaid']:
            recreation = Recreation.objects.get(id=pk)
            recreation.customer = request.user
            recreation.email = request.user.email
            recreation.price = float(data['price'])
            recreation.is_paid = True
            recreation.save()
            
        return redirect('payment-confirmation')


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(email=request.user.email)
        reservations = TableReservation.objects.filter(email= request.user.email)
        recreations = Recreation.objects.filter(email=request.user.email)

        print(orders)
        for order in orders:
            print(order.food)

        context = {
            'orders': orders,
            'reservations': reservations,
            'recreations': recreations,
        }

        return render(request, 'restaurant/dashboard.html', context)
