from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=400)

    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_email(email):
        # get returns only one data filte give all records
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False