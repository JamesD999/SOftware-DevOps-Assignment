from django.contrib import admin
from .models import CreateBaseInfoRecord, CreateOnboardingInfoRecord, CreateContractInfoRecord

admin.site.register(CreateBaseInfoRecord)
admin.site.register(CreateOnboardingInfoRecord)
admin.site.register(CreateContractInfoRecord)

