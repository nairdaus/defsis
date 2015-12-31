from __future__ import unicode_literals
# 
# from django.db import models
# from django.contrib.auth.models import User
# from denuncias.models import Defensoria
# 
# User.add_to_class('access', models.IntegerField(null = True, blank = True))
# User.add_to_class('defensoria', models.ForeignKey(Defensoria, blank = True, null = True))

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
	"""
	Custom user class.
	"""
	acces = models.IntegerField(null = True, blank = True)
	email = models.EmailField('email address', unique=True, db_index=True)
	joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'

	def __unicode__(self):
		return self.email