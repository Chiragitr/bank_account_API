# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models 
from django_extensions.db.models import TimeStampedModel

class bank_account(TimeStampedModel):
	account_holder_name = models.CharField(max_length = 200)
	account_number = models.IntegerField()
	ifsc_code = models.IntegerField()
	branch_name = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.account_holder_name



 
