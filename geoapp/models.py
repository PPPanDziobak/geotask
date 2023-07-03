from django.db import models


class GeometryCoordinatesModel(models.Model):
    x1 = models.IntegerField()
    x2 = models.IntegerField()
    y1 = models.IntegerField()
    y2 = models.IntegerField()
    z1 = models.IntegerField()
    z2 = models.IntegerField()
    plane = models.CharField(max_length=2, default='XY')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

