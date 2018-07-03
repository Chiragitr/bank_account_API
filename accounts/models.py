# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    # def create_user(self, name, password=None):
    #     """
    #     Creates and saves a User with the given email and password.
    #     """
    #     if not name:
    #         raise ValueError('Users must have Name')

    #     user = self.model(
    #         name=self.name,
    #     )

    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_user(self, username, password, **extra_fields):
	    """
	    Creates and saves a user with the given username and password.
	    """
	    if not username:
	        raise ValueError('The given username must be set')
	    username = self.model.normalize_username(username)
	    user = self.model(username=username, **extra_fields)
	    user.set_password(password)
	    user.save(using=self._db)
	    return user



    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    email = models.EmailField(max_length=255)
    
    username = models.CharField(max_length=255,unique=True)
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_number = models.IntegerField(default='123456')
    
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    
    # notice the absence of a "Password field", that's built in.
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin	
	
	@property
	def is_active(self):
		"Is the user active?"
		return self.active








