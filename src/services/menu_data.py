import csv
from typing import Set
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._parse_menu_data(source_path)

    def _parse_menu_data(self, source_path: str) -> Set[Dish]:
        dishes = set()

        with open(source_path, "r", newline="", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                existing_dish = next(
                    (dish for dish in dishes if dish.name == dish_name), None
                )
                if existing_dish is None:
                    new_dish = Dish(dish_name, price)
                    existing_dish = new_dish
                    dishes.add(new_dish)

                ingredient = Ingredient(ingredient_name)
                existing_dish.add_ingredient_dependency(
                    ingredient, recipe_amount
                )

        return dishes
