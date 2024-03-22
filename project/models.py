from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photos',null=True,blank=True)
    image = models.ImageField(upload_to='photos/',null=True,blank=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.project.name}"

class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='documents/',null=True,blank=True)
    description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.project.name}"
