import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from cloud.workshops.models import Workshop
from cloud.users.models import Student

from .models import Inscription, Order

# Create your views here.

class OrderSummaryView(LoginRequiredMixin, DetailView):
    template_name = 'store/order-summary.html'

    def get_object(self):
        order_qs = Order.objects.filter(user=self.request.user, paid=False)
        if order_qs.exists():
            return order_qs[0]
        else:
            order = Order.objects.create(user=self.request.user)
            order.save()
            return order

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, slug):
        student = get_object_or_404(Student, slug=request.POST.get('student'))
        workshop = get_object_or_404(Workshop, slug=slug)

        inscription: Inscription = Inscription.objects.create(
            workshop=workshop,
            user=request.user,
            student=student
        )

        order_qs = Order.objects.filter(user=request.user, paid=False)

        if order_qs.exists():
            order = order_qs[0]
            inscription.order = order
            inscription.save()
        else:
            order = Order.objects.create(
                user=request.user
            )
            order.save()
            inscription.order = order
            inscription.save()

        messages.info(request, "You added an inscription.")
        return redirect("store:order-summary")


class RemoveFromCartView(LoginRequiredMixin, View):
    def get(self, request, pk):
        inscription = get_object_or_404(Inscription, pk=pk)
        inscription.delete()

        messages.info(request, "You removed an inscription.")
        return redirect("store:order-summary")


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        context = {
            'order': order
        }

        return render(request, 'store/checkout.html', context)

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        
        now = datetime.datetime.now()

        for inscription in order.inscriptions.all():
            inscription.paid = True
            inscription.paid_at = now
            inscription.save()
        
        order.paid = True
        order.paid_at = now
        order.save()

        messages.success(request, "Thanks for your purchase! You will receive an email with your receipt.")
        return redirect('/')