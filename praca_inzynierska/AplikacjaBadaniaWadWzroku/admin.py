from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(Test)
admin.site.register(Exercises)
admin.site.register(Information)
admin.site.register(Information1)
