from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from denuncias.models import Defensoria

User.add_to_class('acces', models.IntegerField(null = True, blank = True))
User.add_to_class('defensoria', models.ForeignKey(Defensoria, blank = True, null = True))