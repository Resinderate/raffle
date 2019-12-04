from django.contrib import admin

from tickets.models import Ticket, Player, Session, Class


class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SessionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Ticket)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Class, ClassAdmin)
