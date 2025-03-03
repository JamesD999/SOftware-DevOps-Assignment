from django.db import models

class CreateBaseInfoRecord(models.Model):
    employee_ID = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    DOB = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)



    def __str__(self):
        return f"{self.employee_ID}, {self.first_name} {self.last_name}, {self.DOB}, {self.phone_number}"


class CreateOnboardingInfoRecord(models.Model):
    employee = models.ForeignKey(CreateBaseInfoRecord, on_delete=models.CASCADE)
    health_and_safety = models.CharField(max_length=30)
    fire_drill = models.CharField(max_length=30)
    kpi_creation = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.employee}, {self.fire_drill}, {self.kpi_creation}, {self.health_and_safety}"


class CreateContractInfoRecord(models.Model):
    employee = models.ForeignKey(CreateBaseInfoRecord, on_delete=models.CASCADE)
    annual_wages =models.CharField(max_length=30)
    hours_per_week = models.CharField(max_length=30)
    official_position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee}, {self.official_position}, {self.annual_wages}, {self.hours_per_week}"
