from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    """
    модель Phone с полями id, name, price, image, release_date, lte_exists и slug. Поле id - должно быть основным ключом модели.
    Значение поля slug должно устанавливаться слагифицированным значением поля name.
    """
    id = models.AutoField(primary_key=True, serialize=False),
    name = models.CharField(max_length=64, verbose_name='Модель телефона'),
    price = models.IntegerField(verbose_name='Цена'),
    image = models.ImageField(upload_to='', verbose_name='Изображение'),
    release_date = models.DateField(verbose_name='Дата выпуска'),
    lte_exists = models.BooleanField(verbose_name='Наличие LTE'),
    slug = models.SlugField(blank=True, unique=True, verbose_name='URL'),


