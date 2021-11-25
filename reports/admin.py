from adminsortable.admin import SortableAdmin
from django.contrib import admin
from django import forms

from reports.models import Section, Quote, Tag


class QuoteFormAdmin(admin.ModelAdmin):
    list_display = ('content', 'section')
    list_filter = ('section',)

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'content': forms.Textarea}
        return super().get_form(request, obj, **kwargs)


class QuoteAdmin(QuoteFormAdmin, SortableAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Section, SortableAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Tag, TagAdmin)
