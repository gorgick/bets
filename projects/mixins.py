from django.views.generic.detail import SingleObjectMixin

from customers.models import Customer, Notification
from projects.models import Cart


class CartMixin(SingleObjectMixin):

    def dispatch(self, request, *args, **kwargs):
        self.cart = None
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            cart = Cart.objects.filter(owner=customer).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
            self.cart = cart
        return super(CartMixin, self).dispatch(request, *args, **kwargs)


class NotificationsMixin(SingleObjectMixin):
    @staticmethod
    def notifications(user):
        if user.is_authenticated:
            return Notification.objects.alle(user.customer)
        return Notification.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = self.notifications(self.request.user)
        return context