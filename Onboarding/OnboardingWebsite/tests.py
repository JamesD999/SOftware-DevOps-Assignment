from django.test import TestCase
from .models import CreateBaseInfoRecord, CreateOnboardingInfoRecord, CreateContractInfoRecord

class BaseInfoRecordTest(TestCase):
    def test_create_base_record(self):
        record = CreateBaseInfoRecord.objects.create(
            employee_ID='E48484',
            first_name='Ronald',
            last_name='Weasley',
            DOB='22/01/1987',
            phone_number='1234567890'
        )
        self.assertIsNotNone(record.pk)


class OnboardingInfoRecordTest(TestCase):
    def test_create_onboarding_record(self):
        employee = CreateBaseInfoRecord.objects.create(
            employee_ID='E48484',
            first_name='Ronald',
            last_name='Weasley',
            DOB='22/01/1987',
            phone_number='1234567890'
        )

        record = CreateOnboardingInfoRecord.objects.create(

            employee=employee,
            health_and_safety ='yes',
            fire_drill ='yes',
            kpi_creation = 'no'
        )
        self.assertIsNotNone(record.pk)




class ContractInfoRecordTest(TestCase):
    def test_create_contract_record(self):
        employee = CreateBaseInfoRecord.objects.create(
            employee_ID='E48484',
            first_name='Ronald',
            last_name='Weasley',
            DOB='22/01/1987',
            phone_number='1234567890'
        )

        record = CreateContractInfoRecord.objects.create(
            employee=employee,
            annual_wages='20000',
            hours_per_week='22',
            official_position='Doctor'
        )

        self.assertIsNotNone(record.pk)