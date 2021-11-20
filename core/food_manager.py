from typing import List
import pickle
import pandas as pd
import math

class FoodItem:
    """Food item class"""
    
    def __init__(self, row: pd.Series):
        self.code = str(row["code"])
        self.name = str(row["product_name"]).lower()
        self.tags = self.name.split(" ")
        if row["categories_en"] is not None:
            self.tags += row["categories_en"].split(",")
        self.image_url = str(row["image_url"]).lower()
        self.weight = row["weight"]
        self.packaging_area = float(row["packaging area"])
        self.packaging_materials = []
        if row["glass"]:
            self.packaging_materials.append("glass")
        if row["metal"]:
            self.packaging_materials.append("metal")
        if row["plastic"]:
            self.packaging_materials.append("plastic")
        if row["carton"]:
            self.packaging_materials.append("carton")
        self.store = row["stores"]

    def compute_data_score(self):
        if not hasattr(self, "data_score"):
            #self.data_score = (len(self.tags), -0.5*len(self.packaging_materials) - (1 if not math.isnan(self.packaging_area) else 0))
            self.data_score = len(self.tags)

class FoodManager:

    def __init__(self, food_items: List[FoodItem]):
        # Maps tags to lists of indices that correspond to food's position in food_items
        self.tag_to_food_items = dict()
        self.food_items = food_items
        for id, food_item in enumerate(self.food_items):
            self.init_tag_to_food_items(id, food_item.tags)
        print("Initialized init to tags")

    def get_food_items_by_tag(self, tags, k=10):
        found_items = {}
        for tag in tags:
            if tag in self.tag_to_food_items:
                food_list = self.tag_to_food_items[tag]
                for food_idx in food_list:
                    found_items.setdefault(food_idx, 0)
                    found_items[food_idx] += 1
            else:
                print("Didnt find word", tag)

        # Sort food items by number of occurrences
        l = sorted(found_items.items(), key=lambda x: (x[1], self.food_items[x[0]].data_score))

        return [e[0] for e in l[:k]]

    def init_tag_to_food_items(self, obj_id, tags):
        for s in set(tags):
            self.tag_to_food_items.setdefault(s, [])
            self.tag_to_food_items[s].append(obj_id)


def assemble(food_file="food.pickle"):
    with open(food_file, "rb") as file:
        l = pickle.load(file)
    for item in l:
        item.compute_data_score()
    print("Loaded pickle file")
    manager = FoodManager(l)
    print("Assembled food manager")
    return manager


if __name__ == "__main__":
    manager = assemble()
    print(manager.food_items[0].data_score)
    result = manager.get_food_items_by_tag(["tomato"])
    print(result)
    print([manager.food_items[idx].name for idx in result])
    print([manager.food_items[idx].data_score for idx in result])
    print([manager.food_items[idx].image_url for idx in result])

    print(len(manager.tag_to_food_items["tomato"]))
    print("Finished")