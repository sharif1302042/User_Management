from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class AuxUserManager(BaseUserManager):

    def create_user(self, username, password=None, location=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('User must have an username')
        if location == 'super':
            username = username
        else:
            status, username = is_phone_valid(username)
            if not status:
                raise ValueError("Username value error!")

        user = self.model(
            # username=self.normalize_email(username)
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            password=password,
            location='super'
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_pending = False
        user.save(using=self._db)
        return user

    def make_user_pending_to_not_pending(self, connect_id):
        aux_obj = self.get(username=connect_id)
        aux_obj.is_pending = False
        aux_obj.save()
        return aux_obj

    def pin_reset(self, connect_id):
        aux_obj = self.get(username=connect_id)
        aux_obj.is_pin_reset = True
        aux_obj.save()

class AuxUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='Username',
        unique=True,
        max_length=20,

    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True
    )

    first_name = models.CharField(max_length=50, verbose_name='User first name')
    mid_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='User mid name')
    last_name = models.CharField(max_length=50, verbose_name='User last name')
    join_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    country_code = models.CharField(max_length=10, verbose_name='User country code for mobile number')

    # user boolean field
    is_active = models.BooleanField(default=True)
    is_pending = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_pin_reset = models.BooleanField(default=False)

    objects = AuxUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def full_name(self):
        """
        :return: User full name
        """
        return " ".join(filter(None, (self.first_name, self.mid_name, self.last_name)))

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # @classmethod
    # def make_user_pending_to_not_pending(self):
    #     """
    #     this function takes an username as argument when an agent is verified
    #     then this funtions active the user that is is_pending True to False
    #     :param username: get connent id
    #     :return: the modified user
    #     """
    #     self.is_pending=False
    #     self.save(self)





    # class Meta:
    #     """
    #     You must need to use Postgres SQL DB unless you can't use BrinIndex
    #
    #     """
    #     indexes = (
    #         BrinIndex(fields=['id', 'join_date']),
    #         models.Index(fields=['first_name', 'mid_name', 'last_name']),
    #     )
    #     db_table = 'aux_users'
