from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("User Must have an email address")
        
        if not username:
            raise ValueError("user must have an username")

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)


class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE =(
        (VENDOR,'vendor'),
        (CUSTOMER,"customer"),
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,blank=True,unique=True
    )
    phone=models.CharField(max_length=12,blank=True)
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)

    # required fields
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now_add=True)

    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','first_name','last_name']
   
    objects=UserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role='vendor'
        elif self.role == 2:
            user_role='customer'
        return user_role   




class UserProfile(models.Model):
    # for user have only one profile
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)

    address=models.CharField(max_length=50,blank=True,null=True)
    city=models.CharField(max_length=15,blank=True,null=True)
    pin_code=models.CharField(max_length=6,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
    

