from django.db import models
from datetime import date

class Section(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Loan(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)  # Add a foreign key to Section
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def calculate_interest(self):
        # Calculate the number of days between start_date and end_date
        days_active = (self.end_date - self.start_date).days

        # Calculate the interest based on the formula: interest = (loan_amount * interest_rate * days) / 36500
        interest = (self.amount * self.interest_rate * days_active) / 36500

        return interest

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True)
    INSTALLMENT = 'Installment'
    WHOLE_AMOUNT = 'Whole Amount'
    PAYMENT_CHOICES = [
        (INSTALLMENT, 'Installment'),
        (WHOLE_AMOUNT, 'Whole Amount'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_date = models.DateField()
    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default=INSTALLMENT,
    )
