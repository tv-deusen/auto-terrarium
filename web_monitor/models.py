# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Reading(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return "\nTime: {}\nTemp: {}\nHumidity: {}".format(self.timestamp, self.temperature, self.humidity)

