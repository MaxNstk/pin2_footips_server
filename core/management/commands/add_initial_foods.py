from django.core.management import BaseCommand
from core.models import Food, FoodType
from googletrans import Translator
import csv

class Command(BaseCommand):
    
    def handle(self, *args, **options):

        # if Food.objects.count() > 100:
        #     return
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
                try:
                    description = translator.translate(name, src='en', dest='pt')

                    food = Food(
                        description=description.text,
                        food_type=food_type,
                    )

                    # Convert grams (g) to milligrams (mg) for appropriate fields
                    fields_to_convert = ['calories','serving_size', 'total_fat', 'saturated_fat', 'cholesterol', 'sodium', 'carbohydrate', 'protein']
                    for field in fields_to_convert:
                        value = line[field_indices[field]]
                        if value.endswith('UI') or value.endswith('mg'):
                            value = float(value[:-2])
                        elif value.endswith('mc'):
                            value = float(value[:-2]) / 1000  # Convert micrograms to milligrams
                        elif value.endswith('mcg'):
                            value = float(value[:-3]) / 1000  # Convert micrograms to milligrams
                        elif value.endswith('g'):
                            value = float(value[:-1]) * 1000  # Convert grams to milligrams
                        else:
                            value = float(value) if value else 0
                        setattr(food, field, value)
                        # food.calories = float(line[field_indices['calories']])

                    food.save()
                except Exception as e:
                    print(f"Error processing food '{name}': {str(e)}'")


            # for line in reader:
            #     name = line[field_indices['name']]
            #     try:

            #         description = translator.translate(name, src='en', dest='pt')

            #         Food.objects.get_or_create(
            #             description=description.text,
            #             calories=line[field_indices['calories']],
            #             serving_size=line[field_indices['serving_size']],
            #             total_fat=line[field_indices['total_fat']],
            #             saturated_fat=line[field_indices['saturated_fat']],
            #             cholesterol=line[field_indices['cholesterol']],
            #             sodium=line[field_indices['sodium']],
            #             carbohydrate=line[field_indices['carbohydrate']],
            #             proteins=line[field_indices['protein']],
            #             snack_type=0,
            #             food_type=food_type,
            #         )
            #     except:
            #         continue
