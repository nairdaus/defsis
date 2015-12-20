from __future__ import unicode_literals

from django.db import models
from denuncias.models import Defensoria
from django.contrib.auth.models import User

User.add_to_class('acces', models.IntegerField(null = True, blank = True))
User.add_to_class('defensoria', models.ForeignKey(Defensoria, blank = True, null = True))
