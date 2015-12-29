from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

User.add_to_class('access', models.IntegerField(null = True, blank = True))


# Create your models here.
