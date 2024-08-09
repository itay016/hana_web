from django.contrib import admin
# from reversion.admin import VersionAdmin
from django.apps import apps
from .models import *
from django.contrib.auth.models import User
from core.admin import AllFieldsAdmin


all_models = apps.get_models()

for model in all_models:
    if "Token" in str(model):
        continue
    if not admin.site.is_registered(model):
        try:
            admin.site.register(model, AllFieldsAdmin)
        except:
            pass