from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_the_user, name='logout'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('create_base_info_record/', views.create_base_info_record, name= 'create_base_info_record'),
    path('create_onboarding_training_info_record/', views.create_onboarding_training_info_record, name= 'create_onboarding_training_info_record'),
    path('create_contract_info_record/', views.create_contract_info_record, name= 'create_contract_info_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record')

]
