from django.db import models

class Scene(models.Model):
    scene_id = models.CharField(max_length=20)
    scene_description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.scene_id} - {self.scene_description}"
    
class Object(models.Model):
    scene_id = models.ForeignKey(Scene, on_delete=models.CASCADE)
    dx = models.FloatField()
    dy = models.FloatField()
    
    def __str__(self):
        return f"Object at dx:{self.dx}, dy:{self.dy}"