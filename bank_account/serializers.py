from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *



class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bank_account
        fields = ('url', 'account_holder_name', 'account_number', 'ifsc_code' , 'branch_name')

