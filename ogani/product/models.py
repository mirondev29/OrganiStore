from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('категория', max_length=250, db_index=True, blank=False, null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    slug = models.SlugField('url' ,max_length=250, unique=True, null=True, editable=True)
    created_at = models.DateTimeField('Дата создания' ,auto_now_add=True)

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        full_path = [self.name]
        key = self.parent
        while key is not None:
            full_path.append(key.name)
            key = key.parent
        return ' -> '.join(full_path[::-1])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
        
        

class Product(models.Model):
    name = models.CharField('Продукт', max_length=250, db_index=True, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    slug = models.SlugField('url' ,max_length=250, unique=True, null=True, editable=True)
    description = models.TextField('Описание',blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='products/%Y/%m/%d', blank=True, null=True)
    available = models.BooleanField('Наличие', default=True)
    created_at = models.DateTimeField('Дата создания' ,auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления' ,auto_now=True)

    class Meta:
        unique_together = ('slug', 'category')
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    