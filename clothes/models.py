from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="тег")

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name


class Clothes(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    tags = models.ManyToManyField(Tag, verbose_name="теги")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    class Meta:
        verbose_name = "одежда"
        verbose_name_plural = "одежда"

    def __str__(self):
        return f'{self.title} - {", ".join(tag.name for tag in self.tags.all())}'
