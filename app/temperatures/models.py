from django.db import models
from django.urls import reverse


class Organization(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Temperature(models.Model):
    GENDER_LIST = [
        ("M", 'M'),
        ("F", 'F'),
    ]
    created = models.DateField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    name = models.CharField(max_length=100, null=True)
    organization = models.ForeignKey(
        Organization, related_name="organizations", on_delete=models.SET_NULL, null=True
    )
    nic_no = models.CharField("NIC", max_length=8)
    dob = models.DateField("DOB")
    gender = models.CharField(max_length=1, choices=GENDER_LIST, null=True, blank=True)
    district = models.ForeignKey(
        District, related_name="districts", on_delete=models.SET_NULL, null=True
    )
    address = models.CharField(max_length=100, help_text="Derriere Fort, the Morne")
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def get_temp_alert(self):
        if self.temperature > 37.5:
            return "danger"
        return "success"
    
    def get_address(self):
        return f"{self.address}, {self.district.name}"

    
    def get_absolute_url(self):
        return reverse("temperatures:temperature-detail", kwargs={"pk": self.pk})
    

    class Meta:
        ordering = ("-temperature",)

    def __str__(self):
        return f"{self.temperature}"
