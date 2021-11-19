from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . import forms, models
# Create your views here.


class Index(FormView):
    template_name = 'core/index.html'
    form_class = forms.BirthdayWishForm
    form_name  = 'wish_form'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
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

    