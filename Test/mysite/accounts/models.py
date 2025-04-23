from django.db import models
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    #make sure to test what happens when someone goes over the limit
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    FName = models.CharField(max_length=50, default="")
    LName = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")




    def __str__(self):
        return self.username


class Faculty(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    FName = models.CharField(max_length=50, default="")
    LName = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")

#class Exam(models.Model):
    #ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    #Date = models.DateTimeField(default= timezone.now)
    #ClassNum = models.CharField(max_length=50)
    #Procter = models.ForeignKey(Faculty, on_delete=models.CASCADE)

#class ExamRegistration(models.Model):
    #studentID = models.ForeignKey(Person, on_delete=models.CASCADE)
    #examID = models.ForeignKey(Exam, on_delete=models.CASCADE)




class User(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    email = models.EmailField(primary_key=True)
    nshe = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    name = models.CharField(max_length=100)

class Exam(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=20)
    booked = models.PositiveIntegerField(default=0)

class Registration(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('email', 'exam')



