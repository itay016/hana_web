from django.contrib import admin

from django.apps import apps


class AllFieldsAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.search_fields = [model._meta.fields[0].name, model._meta.fields[
            1].name]
        super(AllFieldsAdmin, self).__init__(model, admin_site)

