from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    photo = models.FileField(null=True)

    def __str__(self):
        return self.name



   #ДЛЯ ПОСЛЕДНЕГО ЗАДАНИЯ
# class Posts(models.Model):
#     title = models.CharField(max_length=20)
#     text = models.CharField(max_length=500)