# from django.db import models

# # Create your models here.

# class StateSnapProgram(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
    

# class ApplicationInfo(models.Model):
#     Description = models.CharField(max_length=255)
#     Link = models.URLField()

#     def __str__(self):
#         return self.Description

# class SnapData(models.Model):
#     Organization = models.CharField(max_length=255)
#     SubPrograms = models.CharField(max_length=255) #this would have more but for snap data, it only has one
#     StateSNAPProgramName = models.ManyToManyField(StateSnapProgram)  # Many-to-many relationship
#     SNAPWebsite = models.URLField()
#     Applications = models.ManyToManyField(ApplicationInfo)  # Many-to-many relationship
#     StateEBTInfo = models.URLField()

#     def __str__(self):
#         return self.Organization

from django.db import models

class StateSnapProgram(models.Model):
    StateSNAPProgramName = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SnapData(models.Model):
    Organization = models.CharField(max_length=255, default="Organization")
    SubPrograms = models.CharField(max_length=255, default="Supplemental Nutrition Assistance Program (SNAP)")  # Many-to-many relationship
    StateSNAPProgramName = models.ManyToManyField(StateSnapProgram)  # Many-to-many relationship
    SNAPWebsite = models.URLField(default="snapwebsite")
    StateEBTInfo = models.URLField(default="ebtwebsite")

    def __str__(self):
        return self.Organization


class ApplicationInfo(models.Model):
    Description = models.CharField(max_length=255, default="description here")
    Link = models.URLField(default="application link here")

    def __str__(self):
        return self.Description
