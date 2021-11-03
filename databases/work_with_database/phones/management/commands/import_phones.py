import csv
from pprint import pprint

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_list = []
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for line in phone_reader:
                # # TODO: Добавьте сохранение модели
                # phone.name = line[1]
                # phone.image = line[2]
                # phone.price = line[3]
                # phone.release_date = line[4]
                # phone.lte_exists = line[5]
                # phone.slug = slugify(line[1])
                # phone.save()
                # #
                phone = Phone.objects.create(
                    name=line[1],
                    image=line[2],
                    price=line[3],
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slugify(line[1]))
                # phone.save()
                phone_list.append(phone)
        pprint(phone_list)
