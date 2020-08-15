from django.contrib import messages, admin
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from broker.wallet import Wallet

from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.contrib.admin.sites import site
from django.utils.text import Truncator
from django.utils.html import escape
from django import forms
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponsePermanentRedirect


class WalletAdmin(admin.ModelAdmin):
    search_fields = ('id', 'cod_active')
    list_display = ( 'id', 'cod_active', 'vl_ultimo', 'variacao', 'time_purchase', 'quantity', 'times',
                     'purchased', 'intention_buy','stop_loss', 'stop_gain')
    list_display_links = ('cod_active', 'vl_ultimo', 'variacao', 'time_purchase')
    ordering = ('cod_active', '-purchased', '-intention_buy', '-variacao')
    # raw_id_fields = ('active',)


admin.site.site_header = 'Hedging admin'
admin.site.register(Wallet, WalletAdmin)