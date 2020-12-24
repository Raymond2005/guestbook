from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MessageList(ListView):
    model = Message

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('msg_list')

class MessageDelete(LoginRequiredMixin,DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')