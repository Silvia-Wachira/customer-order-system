from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from core.abstract.models import AbstractModel, AbstractManager

# Custom manager for the User model that provides methods to create users
class UserManager(BaseUserManager,AbstractManager):
        
    def create_user(self, username, email, password=None,**kwargs):
        """Create and return a `User` with an email, phonenumber, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have a password.')
        
         # Create a new user instance, normalize the email, and set the password
        user = self.model(username=username,email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
# Custom User model extending AbstractBaseUser and PermissionsMixin
class User(AbstractBaseUser, AbstractModel,PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True,default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True,max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    phone_number = models.IntegerField(unique=True, null=True)
    password = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    # Property to return the user's full name
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
