from django.core.management.base import BaseCommand
import csv
from profstandart.models import ProfessionalType, ProfessionalArea, ProfStandart
from django.conf import settings
from datetime import datetime

class Command(BaseCommand):
    help = 'загрузка csv файла с профстандартами в базу приложения'

    def handle(self, *args, **options):
        
        if not args:
            filepath = settings.BASE_DIR / 'профстандарт.csv'
        else:
            filepath = settings.BASE_DIR / args[0]

        with open(filepath.as_posix(), encoding='utf-8') as fp:
            reader = csv.DictReader(fp, delimiter=';', quoting=csv.QUOTE_ALL)
            for line in reader:
                cod = line['standard_code']
                is_exist = ProfStandart.objects.filter(cod=cod)
                if is_exist:
                    continue
                profstd = ProfStandart()
                profstd.regnum = int(line['standard_number'])
                profstd.cod = cod
                profstd.title = line['standard_name']
                try:
                    profarea, _ = ProfessionalArea.objects.get_or_create(name=line['professional_area'])
                except:
                    print('Сфера деятельности слишком длинная')
                    print(line['professional_area'])
                    raise Exception('Сфера деятельности слишком длинная')
                profstd.profarea = profarea
                try:
                    proftype, _ = ProfessionalType.objects.get_or_create(name=line['professional_type'])
                except:
                    print('Тип профессии слишком длинный')
                    print(line['professional_type'])
                    raise Exception('Тип профессии слишком длинный')
                profstd.proftype = proftype
                numorder, _ , numdate = line['order_Mintrud'].split(' ')
                profstd.numorder = numorder
                profstd.dateorder = datetime.strptime(numdate, '%d.%m.%Y')
                
                profstd.save()
        


    def add_arguments(self, parser):
        parser.add_argument(
        nargs='+',
        type=str,
        dest = 'args'
        )