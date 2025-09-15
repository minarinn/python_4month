from django.db import models

class Book(models.Model):
    GENRES = (
        ('роман', 'роман'),
        ('фантастика', 'фантастика'),
        ('фэнтези', 'фэнтези'),
        ('нон фикшн', 'нон фикшн'),
        ('детектив', 'детектив'),
    )

    title = models.CharField(max_length=100, verbose_name='название книги')
    author = models.CharField(max_length=100, verbose_name='автор')
    description = models.TextField(verbose_name='описание')
    publish_date = models.DateField(verbose_name='дата публикации')
    pages = models.IntegerField(verbose_name='количество страниц')
    cover = models.ImageField(upload_to='books/', verbose_name='обложка')
    genre = models.CharField(max_length=50, choices=GENRES, default='роман')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена')
    language = models.CharField(max_length=50, verbose_name='язык')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Review(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name='выберите книгу')
    text = models.TextField(verbose_name='оставьте отзыв')
    stars = models.CharField(max_length=100, choices=STARS, verbose_name='поставьте оценку о книге', default='⭐⭐⭐⭐')

    def __str__(self):
        return f'{self.book} - {self.stars}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
