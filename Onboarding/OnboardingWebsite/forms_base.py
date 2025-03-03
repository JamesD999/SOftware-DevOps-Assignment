from django import forms
from .models import CreateBaseInfoRecord


class CreateBaseInfoRecordForm(forms.ModelForm):

    employee_ID = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={"placeholder":"EmployeeID", "class":"form-control"}), label= "")
    first_name = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label= "")
    last_name = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label= "")
    DOB = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={"placeholder":"DOB", "class":"form-control"}), label= "")
    phone_number = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label= "")


    class Meta:
        model = CreateBaseInfoRecord
        exclude=("user",)