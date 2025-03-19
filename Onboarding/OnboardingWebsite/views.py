from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms_base import CreateBaseInfoRecordForm
from .forms_contract import CreateContractInfoRecordForm
from .forms_onboarding import CreateOnboardingInfoRecordForm
from .models import CreateBaseInfoRecord, CreateOnboardingInfoRecord, CreateContractInfoRecord
from django.contrib.auth import authenticate, login, logout

def home(request):

    BaseRecords = CreateBaseInfoRecord.objects.all()
    OnboardingRecords = CreateOnboardingInfoRecord.objects.all()
    ContractRecords = CreateContractInfoRecord.objects.all()

   # AllRecords = list(BaseRecords) + list(OnboardingRecords) + list(ContractRecords)
    AllRecords =list(CreateOnboardingInfoRecord.objects.select_related('employee').all())


    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Login error. Invalid username or password.")
            return redirect('home')

    return render(request, 'home.html', {'AllRecords': AllRecords})

def logout_the_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('home')



def create_base_info_record(request):
    form1 = CreateBaseInfoRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form1.is_valid():
                form1.save()
                messages.success(request, "Base Info Record added")
                return redirect('home')
        return render(request, 'create_base_info_record.html', {'form1': form1})
    else:
        messages.error(request, "You are not logged in")
        return redirect('home')

def create_onboarding_training_info_record(request):
    form2 = CreateOnboardingInfoRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form2.is_valid():
                form2.save()
                messages.success(request, "Onboarding Info Record added")
                return redirect('home')
        return render(request, 'create_onboarding_info_record.html', {'form2': form2})
    else:
        messages.error(request, "You are not logged in")
        return redirect('home')

def create_contract_info_record(request):
    form3 = CreateContractInfoRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form3.is_valid():
                form3.save()
                messages.success(request, "Contract Info Record added")
                return redirect('home')
        return render(request, 'create_contract_info_record.html', {'form3': form3})
    else:
        messages.error(request, "You are not logged in")
        return redirect('home')



def delete_record(request, pk):
    if request.user.is_authenticated:
        try:
            basic_delete_this_record = get_object_or_404(CreateBaseInfoRecord, pk=pk)
            basic_delete_this_record.delete()
            messages.success(request, "Employee record and all related records (onboarding, contract) deleted successfully.")
        except CreateBaseInfoRecord.DoesNotExist:
            messages.warning(request, "Employee record not found.")

        return redirect('home')
    else:
        messages.error(request, "Please login to delete records.")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        basic_record = get_object_or_404(CreateBaseInfoRecord, id=pk)
        messages.success(request, basic_record.first_name)
        basic_record.first_name= "bob"
        basic_record.save()



        return redirect('home')
    else:
        messages.error(request, "Please login to delete records.")
        return redirect('home')


