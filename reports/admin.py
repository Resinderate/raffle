from adminsortable.admin import SortableAdmin
from django.contrib import admin

from reports.models import Section, Quote


admin.site.register(Section, SortableAdmin)
admin.site.register(Quote, SortableAdmin)
