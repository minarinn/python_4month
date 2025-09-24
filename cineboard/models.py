from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name

class Films(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Хоррор', 'Хоррор'),
        ('Драма', 'Драма'),
        ('Комедия', 'Комедия'),
    )
    title = models.CharField(max_length=100, default='фильм1')
    description = models.TextField(default='Описание фильма')
    genre = models.CharField(max_length=100, choices=GENRE, default='Фантастика')
    release_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title

class Rating(models.Model):
    MARKS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    choice_films = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='rating')
    stars = models.CharField(max_length=2, choices=MARKS, default='3', null=True)
    text = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return f"{self.choice_films.title} — {self.stars}★"