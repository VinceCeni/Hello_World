from django.db import models

TYPE_CHOICES = {
    ('Mr.','Mr.'),
    ('Mrs.','Mrs.'),
    ('Ms.','Ms.'),
}

class profiles(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES, default="", blank=True, null=False)
    firstname = models.CharField(max_length=60, default="", blank=True, null=False)
    lastname = models.CharField(max_length=60, default="", blank=True, null=False)
    Email = models.CharField(max_length=60, default="", blank=True, null=False)
    username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.firstname