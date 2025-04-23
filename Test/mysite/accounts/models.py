from django.db import models
from django.utils import timezone
# Create your models here.





class User(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    email = models.EmailField(primary_key=True)
    nshe = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    name = models.CharField(max_length=100)


class Registration(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('email', 'exam')



# ========================
# Authentication Table
# ========================
class Authentication(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.email


# ========================
# Student Table
# ========================
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nshe = models.CharField(max_length=20, unique=True)
    auth = models.OneToOneField(Authentication, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ========================
# Faculty Table
# ========================
class Faculty(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ========================
# Location Table
# ========================
class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    campus = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    room = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.campus} - {self.building} Room {self.room}"


# ========================
# Exam Table
# ========================
class Exam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    capacity = models.PositiveIntegerField(default=20)
    booked = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} on {self.date}"


# ========================
# Exam Registration Table
# ========================
class ExamRegistration(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('student', 'exam')

    def __str__(self):
        return f"{self.student} registered for {self.exam}"


