# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BankSerializer
from .models import *

class BankViewSet(viewsets.ModelViewSet):
  
    queryset = bank_account.objects.all()
    serializer_class = BankSerializer

