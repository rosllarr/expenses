from django.contrib import admin

from .models import Monthly, Tag


class MonthlyAdmin(admin.ModelAdmin):
    list_display = ['title', 'transection_date', 'cost', 'all_tag']

    def all_tag(self, obj):
        return " | ".join([t.name for t in obj.tags.all()])


admin.site.register(Monthly, MonthlyAdmin)
admin.site.register(Tag)
