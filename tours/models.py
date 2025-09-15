from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='ваше имя')
    email = models.EmailField(verbose_name='ваша почта', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Tour(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='tour', verbose_name='участник')
    title = models.CharField(max_length=100, default='Конный тур по Ала-Арче', verbose_name='название тура')
    date = models.DateField(verbose_name='дата тура', default='2025-09-20')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person} - {self.title}'

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
