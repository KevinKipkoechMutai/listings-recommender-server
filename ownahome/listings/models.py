from django.db import models

# Creating models

#listings model
class Listing(models.Model):

    #development status
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('under_construction', 'Under Construction'),
        ('offplan', 'Off-plan'),
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price_cash = models.DecimalField(max_digits=15, decimal_places=2)
    price_mortgage = models.DecimalField(max_digits=15, decimal_places=2)
    development_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


#user information to help calculate property affordability
class UserProfile(models.Model):
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    existing_loans = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
