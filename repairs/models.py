from django.db import models


class Repair(models.Model):
    date = models.DateTimeField(auto_now_add=True),
    status = models.CharField(max_length=100, default="pending", choices=["pending", "completed", "cancelled"]),
   
 


    def __str__ (self):
        return self.email
