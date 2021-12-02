import logging
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView, DetailView
from typing import Dict, Any
from django.views.generic.edit import FormView
from . import forms, models
# Create your views here.

logger = logging.getLogger(__name__)


class Index(FormView):
    template_name = 'core/index.html'
    form_class = forms.BirthdayWishForm
    form_name  = 'wish_form'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['picture_categories'] = models.PictureCategory.objects.all()
        context['project_categories'] = models.ProjectCategory.objects.all()
        
        try:
            context['wish_form'] = self.wish_form
        except:
            context['wish_form'] = self.prepopulate_wish_form()
        return context

    def prepopulate_wish_form(self):
        initial = {
            'info': models.MyInformation.objects.all().first()
        }
        return forms.BirthdayWishForm(initial=initial)

    def form_valid(self, form):
        messages.success(self.request, "Your message was successfully sent.")
        form.save()
        return redirect('core:index')

    def form_invalid(self, form):
        messages.error(self.request, "An error occured.")
        self.wish_form = form
        return self.get(self.request)


class MessageView(FormView):
    form_class = forms.MessageForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Message successfully sent!")
        return redirect('core:index')
    
    def form_invalid(self, form):
        messages.success(self.request, f"An error occured!<br>{form.errors}<br>Try again.")
        return redirect('core:index')


class SendMoney(FormView):
    form_class = forms.TransactionFrom
    template_name = 'core/send-money.html'

    def form_valid(self, form: forms.TransactionFrom) -> HttpResponse:
        transaction = form.save()
        messages.success(self.request, "New Transaction created!")
        return redirect(reverse('core:pay-confirm', kwargs={"pk": transaction.pk}))

    def form_invalid(self, form: forms.TransactionFrom) -> HttpResponse:
        messages.error(self.request, "Unabel to created new transaction")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['send_money'] = True
        return context


class PayConfrim(DetailView):

    template_name = 'core/send-money.html'
    context_object_name = 'transaction'
    model = models.Transaction


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        transaction = models.Transaction.objects.get(pk=self.kwargs['pk'])
        transaction.verify_payment()
        context = super().get_context_data(**kwargs)
        context['context'] = transaction
        context['pay_confirm'] = True
        context['paystack_public_key'] = settings.PAYSTACK_PUBLIC_KEY
        return context

def bounce(request, pk):
    return redirect(reverse('core:pay-confrim', kwargs={'pk': pk}))


class Portfolio(DetailView):
    template_name = 'core/portfolio-details.html'
    model = models.Project