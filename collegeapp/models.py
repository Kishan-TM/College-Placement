from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    pswd=models.CharField(max_length=20,default="")
    date_of_birth=models.DateField(null=True,blank=True)
    phn = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    student_class = models.CharField(max_length=50,null=True)  # "class" is a reserved keyword in Python
    course = models.CharField(max_length=255,null=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    supply = models.CharField(max_length=200,null=True)
    picture = models.ImageField(upload_to='student_pictures/', null=True, blank=True)
    verified = models.BooleanField(default=False)

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    pswd=models.CharField(max_length=20,default="")
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)  # Tutor's qualification
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    subject = models.CharField(max_length=255)  # Subject the tutor teaches
    resume = models.FileField(upload_to='tutor_resumes/', null=True, blank=True)
    is_approved= models.BooleanField(default=False)
    status = models.CharField(max_length=100, default='Pending')

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    qualifications = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    course = models.CharField(max_length=255)

class JobApplication(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

class TrainingSession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255) 
    attendees = models.ManyToManyField(Student, blank=True)