# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Reg.models import UserData


class OTP(models.Model):
    phone = models.ForeignKey(UserData, db_column='UserData.id')
    otp = models.BigIntegerField(id(None))
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.phone