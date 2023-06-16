from typing import Iterable, Optional
from django.db import models
from slugify import slugify

# Create your models here.

class Category(models.Model):
    slug = models.SlugField(primary_key=True, blank=True)
    title = models.CharField(unique=True, max_length=100)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

# class sasg(models.Model):
#     hello = models.CharField(max_length=34)


#     def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
#         return super().save(force_insert, force_update, using, update_fields)