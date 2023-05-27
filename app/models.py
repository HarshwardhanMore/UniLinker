from django.db import models

# Create your models here.


class Database(models.Model):
    user = models.TextField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    phoneNumber = models.TextField()
    linkedIn = models.TextField()
    gitHub = models.TextField()
    instagram = models.TextField()
    facebook = models.TextField()
    resume = models.FileField(upload_to='resumes', default=None)
    resumeFileName = models.TextField()

    def __str__(self):
        return self.name + self.phoneNumber
