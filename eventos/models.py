from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=300)

class Type(models.Model):
    name= models.CharField(max_length=200)

class Event(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    name = models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    place= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    start_date=models.DateTimeField()
    finish_date=models.DateTimeField()
    type=models.ForeignKey(Type, on_delete=models.CASCADE)

""""
    def save(self, *args, **kwargs):


        super().save(*args, **kwargs)  # Call the "real" save() method.

    def modify(self, **kwargs):
        try:
            updatedFields = []
            for key in list(kwargs):
                if kwargs[key]:
                    if key == "residencePlace":
                        value = ResidencePlace(id = kwargs[key])
                    else:
                        value = kwargs[key]
                    setattr(self, key, value)
                    updatedFields.append(key)
            self.save(update_fields = updatedFields)
        except:
            return False
        return True
"""