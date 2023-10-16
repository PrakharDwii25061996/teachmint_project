from django.db import models
# from django.contrib.auth.models import UserManager
from django.contrib.auth.models import  (
    AbstractBaseUser, BaseUserManager
)
# Native app modules
from .managers import CustomerManager


class CustomUser(AbstractBaseUser):
    """
    Table of Customer model inheriting AbstractUser
    """
    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    # Full name of a registered user
    full_name = models.CharField(
        max_length=259,
    )

    # Email of a registered user
    email = models.EmailField(
        max_length=50,
        unique=True,
    )

    # User phone number
    mobile_number = models.CharField(
        max_length=50, blank=True
    )

    # State of a registered user
    password = models.CharField(
        max_length=259,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomerManager()

    #======================================================================================
    def get_short_name(self) -> str:
        # The user is identified by their email address
        return self.email

    def __str__(self) -> str:
        """ string representation of Customer instance """
        return f'{self.full_name}'


class OweOver(models.Model):
    user_owes = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='owe'
    )
    percent_value = models.DecimalField(
        decimal_places=2, max_digits=8, null=True
    )
    amount = models.DecimalField(
        decimal_places=2, max_digits=8, null=True, default=0
    )


class Liability(models.Model):
    EXPENSE_TYPE_CHOICES = (
        ('EQUAL', 'EQUAL'),
        ('EXACT', 'EXACT'),
        ('PERCENT', 'PERCENT')
    )

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='liability'
    )
    expense = models.DecimalField(decimal_places=2, max_digits=7)
    expense_type = models.CharField(max_length=50, choices=EXPENSE_TYPE_CHOICES)
    spent_in_ownself = models.DecimalField(decimal_places=2,  max_digits=7, null=True)
    owe_over = models.ManyToManyField(OweOver, related_name='owe_over', null=True)
