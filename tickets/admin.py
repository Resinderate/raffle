from django.contrib import admin

from tickets.models import Ticket, Player, Session


admin.site.register(Ticket)
admin.site.register(Player)
admin.site.register(Session)
