from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from audiofield.models import AudioFile


class UserManager(BaseUserManager):
	"""
	A custom user manager to deal with emails as unique identifiers for auth
	instead of usernames. The default that's used is "UserManager"
	"""
	def create_user(self, email, profile_picture=None, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
		    raise ValueError('Users must have an email address')

		user = self.model(
		    email=self.normalize_email(email),
		    profile_picture=profile_picture,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, profile_picture=None, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(
		    email,
		    password=password,
		    profile_picture=profile_picture,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    profile_picture = models.ImageField(
        upload_to='user_data/profile_picture', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class Track(AudioFile):
    artist = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        upload_to='upload/audiofiles_img', null=True, blank=True)
    RATING_CHOICE = (
        (1, "Ужасно"),
        (2, "Плохо"),
        (3, "Нормально"),
        (4, "Хорошо"),
        (5, "Отлично"), )
    rating = models.IntegerField(choices=RATING_CHOICE, default=5)
