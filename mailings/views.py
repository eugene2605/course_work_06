from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from mailings.forms import MailingForm, ClientForm
from mailings.models import Mailing, Client


@cache_page(60)
def home(request):
    blog_list = Blog.objects.all()[:3]
    mailings_all = Mailing.objects.count()
    mailings_started = Mailing.objects.filter(status='started').count()
    client_all = Client.objects.distinct().count()
    context = {
        'blog_list': blog_list,
        'mailings_all': mailings_all,
        'mailings_started': mailings_started,
        'client_all': client_all,
    }

    return render(request, 'mailings/home.html', context)


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save
        return super().form_valid(form)


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailings:view_mailing', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save
        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:home')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:create_mailing')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save
        return super().form_valid(form)


class ClientListView(ListView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:list_client')


def mailing_toggle_activity(request, pk):
    mailing_item = get_object_or_404(Mailing, pk=pk)
    if mailing_item.status != 'done':
        mailing_item.status = 'done'
    else:
        mailing_item.status = 'started'

    mailing_item.save()

    return redirect(reverse('mailings:list_mailing'))
