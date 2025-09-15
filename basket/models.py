from django.db import models
from books.models import Book

class Order(models.Model):
    STATUS_CHOICES = (
        ('Выполнено', 'Выполнено'),
        ('Не выполнено', 'Не выполнено'),
    )

    name = models.CharField(max_length=100, verbose_name='Имя')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    card_number = models.CharField(max_length=20, verbose_name='Номер карты')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders', verbose_name='Выберите книгу')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Не выполнено', verbose_name='Статус заказа')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.book.title} - {self.status}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

