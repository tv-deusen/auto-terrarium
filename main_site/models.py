# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Reading(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
