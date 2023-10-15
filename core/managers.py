""" apps/user/managers.py 

	This modules contains some model manager classes

	* class : CustomerManager

"""
from django.contrib.auth.models import  (
    BaseUserManager
)


class CustomerManager(BaseUserManager):
    """
    Customer Registration manager
    """
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))

        if kwargs.get('full_name'):
            user.full_name = kwargs.get('full_name')
        if kwargs.get('email'):
            user.email = kwargs.get('email')
        if kwargs.get('address'):
            user.address = kwargs.get('address')
        if kwargs.get('phone'):
            user.phone = kwargs.get('phone')
        if kwargs.get('country'):
            user.country = kwargs.get('country')
        if kwargs.get('state'):
            user.state = kwargs.get('state')
        if kwargs.get('district'):
            user.district = kwargs.get('district')
        if kwargs.get('is_active'):
            user.is_active = kwargs.get('is_active')
        if kwargs.get('is_staff'):
            user.is_staff = kwargs.get('is_staff')
        if kwargs.get('is_admin'):
            user.is_admin = kwargs.get('is_admin')

        user.admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
