from __future__ import unicode_literals

from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    name = models.CharField(max_length=255, blank=True)

class InternalTicket(Ticket):
    user = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)

class CustomerTicket(Ticket):
    product = models.TextField(blank=True)
