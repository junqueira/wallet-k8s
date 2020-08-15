# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import *
from django.db.models import Sum, Max
from django.contrib import messages
from django.db import transaction
from django.conf import settings


STATUS_WALLET = (('B', 'Buy'),
                 ('S', 'Sell'),
                 ('IB', 'Intention Buy'),
                 ('IS', 'Intention Sell'))

class Wallet(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    # active = models.ForeignKey(Trade)
    cod_active = models.CharField(max_length=10)
    type_option = models.CharField(max_length=2, choices=STATUS_WALLET)
    intention_buy = models.BooleanField(default=False, db_index=True)
    vl_ultimo = models.DecimalField(max_digits=8, decimal_places=2)
    variacao = models.DecimalField(max_digits=8, decimal_places=2)
    time_purchase = models.DateTimeField('time_purchase', null=True, blank=True)
    # creation_date = models.DateTimeField(auto_now_add=True)
    # last_update = models.DateTimeField(auto_now=True)
    purchased = models.BooleanField(default=False, db_index=True)
    stop_loss = models.DecimalField(max_digits=8, decimal_places=2)
    stop_gain = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    times = models.IntegerField()
    observation = models.TextField(help_text='')

    # def __unicode__(self):
    #     return self.active
    #
    # class Meta:
    #     # managed = True
    #     # abstract = True
    #     db_table = 'broker_wallet'
