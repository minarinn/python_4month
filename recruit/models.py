from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('М', 'М'),
    ('Ж', 'Ж')
)

class CustomUser(User):
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)

    EDUCATION_CHOICES = [
        ('hs', 'среднее'),
        ('ba', 'высшее'),
        ('ms', 'магистратура'),
        ('phd', 'докторантура'),
    ]
    education_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES, blank=True, null=True)

    experience_years = models.PositiveIntegerField(default=0)
    desired_position = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    class Meta:
        verbose_name = "кандидат"
        verbose_name_plural = "кандидаты"

    def __str__(self):
        return self.username
