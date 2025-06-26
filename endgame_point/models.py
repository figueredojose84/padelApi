from django.db import models

# Create your models here.
class Point(models.Model):
    dis1Equipo1 = models.IntegerField(default=0)
    dis2Equipo1 = models.IntegerField(default=0)
    dis3Equipo1 = models.IntegerField(default=0)
    dis4Equipo1 = models.IntegerField(default=0)
    dis5Equipo1 = models.IntegerField(default=0)
    dis1Equipo2 = models.IntegerField(default=0)
    dis2Equipo2 = models.IntegerField(default=0)
    dis3Equipo2 = models.IntegerField(default=0)
    dis4Equipo2 = models.IntegerField(default=0)
    dis5Equipo2 = models.IntegerField(default=0)

    
    
    def __str__(self):
        return f"Point({self.dis1Equipo1}, {self.dis2Equipo1}, {self.dis3Equipo1}, {self.dis4Equipo1}, {self.dis5Equipo1}, {self.dis1Equipo2}, {self.dis2Equipo2}, {self.dis3Equipo2}, {self.dis4Equipo2}, {self.dis5Equipo2})"

