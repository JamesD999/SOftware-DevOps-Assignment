from django import forms
from .models import CreateOnboardingInfoRecord


class CreateOnboardingInfoRecordForm(forms.ModelForm):
    health_and_safety =forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={"placeholder":"Health and Safety", "class":"form-control"}), label= "")
    fire_drill = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={"placeholder":"Fire Drill", "class":"form-control"}), label= "")
    kpi_creation = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={"placeholder":"KPI creation", "class":"form-control"}), label= "")

    class Meta:
        model = CreateOnboardingInfoRecord
        exclude=("user",)
