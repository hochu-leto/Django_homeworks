from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    """
    модель Phone с полями id, name, price, image, release_date, lte_exists и slug. Поле id - должно быть основным ключом модели.
    Значение поля slug должно устанавливаться слагифицированным значением поля name.
    """
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.TextField(verbose_name='Модель телефона', default=' ')
    price = models.IntegerField(verbose_name='Цена', default=0)
    image = models.ImageField(upload_to='', verbose_name='Изображение', default='C:\\Users\\Тимофей\\PycharmProjects'
                                                                                '\\Django\\dj-homeworks\\databases'
                                                                                '\\work_with_database\\телефон.png')
    release_date = models.DateField(verbose_name='Дата выпуска', default='1/1/2001')
    lte_exists = models.TextField(verbose_name='Наличие LTE', default='Нет')
    slug = models.SlugField(blank=True, unique=True, verbose_name='URL')


