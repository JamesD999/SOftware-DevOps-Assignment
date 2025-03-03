from django import forms
from .models import CreateContractInfoRecord


class CreateContractInfoRecordForm(forms.ModelForm):



    class Meta:
        model = CreateContractInfoRecord
        exclude=("user",)