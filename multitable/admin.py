# -*- coding: utf-8 -*-
from django.contrib import admin

from multitable.models import Ticket, InternalTicket, CustomerTicket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (u'id', u'title', u'description', u'name')
    search_fields = (u'name',)


@admin.register(InternalTicket)
class InternalTicketAdmin(admin.ModelAdmin):
    list_display = (u'id', u'title', u'description', u'name', u'user')
    list_filter = ('user',)
    search_fields = (u'name',)


@admin.register(CustomerTicket)
class CustomerTicketAdmin(admin.ModelAdmin):
    list_display = (u'id', u'title', u'description', u'name', u'product')
    search_fields = (u'name',)
