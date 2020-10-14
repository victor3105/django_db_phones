import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # print(line)
                id = int(line[0])
                name = line[1]
                image = line[2]
                price = int(line[3])
                date = datetime.strptime(line[4], '%Y-%m-%d').date()
                lte_exists = bool(line[5])
                phone = Phone(id=id, name=name, image=image, price=price,
                              release_date=date, lte_exists=lte_exists)
                phone.save()
