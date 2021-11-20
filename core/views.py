import logging
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView, DetailView
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


class Portfolio(DetailView):
    template_name = 'core/portfolio-details.html'
    model = models.Project