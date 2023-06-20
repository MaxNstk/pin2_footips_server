from django.core.management import BaseCommand
from core.models import Food, FoodType
from googletrans import Translator
import csv

class Command(BaseCommand):
    
    def handle(self, *args, **options):

        if Food.objects.count() > 100:
            return
        translator = Translator(service_urls=['translate.google.com'])
        food_type, created = FoodType.objects.get_or_create(description='Não especificado')

        with open('./docs/nutrition.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

            field_indices = {
                'name': header.index('name'),
                'calories': header.index('calories'),
                'serving_size': header.index('serving_size'),
                'total_fat': header.index('total_fat'),
                'saturated_fat': header.index('saturated_fat'),
                'cholesterol': header.index('cholesterol'),
                'sodium': header.index('sodium'),
                'carbohydrate': header.index('carbohydrate'),
                'protein': header.index('protein'),
            }

            for line in reader:
                name = line[field_indices['name']]
                description = translator.translate(name, src='en', dest='pt')

                Food.objects.create(
                    description=description.text,
                    calories=line[field_indices['calories']],
                    serving_size=line[field_indices['serving_size']],
                    total_fat=line[field_indices['total_fat']],
                    saturated_fat=line[field_indices['saturated_fat']],
                    cholesterol=line[field_indices['cholesterol']],
                    sodium=line[field_indices['sodium']],
                    carbohydrate=line[field_indices['carbohydrate']],
                    proteins=line[field_indices['protein']],
                    snack_type=0,
                    food_type=food_type,
                )
