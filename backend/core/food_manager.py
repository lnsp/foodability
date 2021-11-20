from typing import List
from .utils import RenameUnpickler
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
        self.packaging_materials = row["materials"].split(",")
        self.store = row["stores"]

    def compute_data_score(self):
        if not hasattr(self, "data_score"):
            #self.data_score = (len(self.tags), -0.5*len(self.packaging_materials) - (1 if not math.isnan(self.packaging_area) else 0))
            self.data_score = len(self.tags)
    
    def get_packaging(self, amt=1):
        amt = math.ceil(amt)
        plastic = 0
        metal = 0
        carton = 0
        glass = 0
        pa = max(self.packaging_area, 3.)
        if "plastic" in self.packaging_materials:
            plastic += pa * amt
        if "metal" in self.packaging_materials:
            metal += pa * amt
        if "carton" in self.packaging_materials:
            carton += pa * amt
        if "glass" in self.packaging_materials:
            glass += pa * amt
        return plastic, metal, carton, glass
            

class FoodManager:

    def __init__(self, food_items: List[FoodItem], basic_items: List[FoodItem]=[]):
        # Maps tags to lists of indices that correspond to food's position in food_items
        self.tag_to_food_items = dict()
        self.food_items = food_items + basic_items
        self.basic_items = basic_items
        #Only allow items with a weight
        self.filter_by_has_weight()
        
        for id, food_item in enumerate(self.food_items):
            self.init_tag_to_food_items(id, food_item.tags)
        print("Initialized init to tags")

    def filter_by_has_weight(self):
        ret = []
        for fi in self.food_items:
            if not math.isnan(fi.weight):
                ret.append(fi)
        self.food_items = ret

    def get_food_items_by_tag(self, tags, k=10):
        found_items = {}
        for tag in tags:
            if tag in self.tag_to_food_items:
                food_list = self.tag_to_food_items[tag]
                for food_idx in food_list:
                    found_items.setdefault(food_idx, 0)
                    found_items[food_idx] += 1
            else:
                #print("Didnt find word", tag)
                pass

        # Sort food items by number of occurrences
        # In ascending order
        num_normal_food = len(self.food_items) - len(self.basic_items)
        l = sorted(
            found_items.items(),
            key=lambda x: (-x[1], len(self.food_items[x[0]].tags) + (0 if x[0] < num_normal_food else -10)))

        return [e[0] for e in l[:k]]
    
    def get_food_item_by_tag(self, tags):
        food = self.get_food_items_by_tag(tags, k=1)
        if len(food) > 0:
            print(tags, self.food_items[food[0]].name, self.food_items[food[0]].weight)
            for x in self.get_food_items_by_tag(tags):
                print("Alternative", self.food_items[x].name, self.food_items[x].weight)
            return self.food_items[food[0]]
        else: 
            return None

    def init_tag_to_food_items(self, obj_id, tags):
        for s in set(tags):
            self.tag_to_food_items.setdefault(s, [])
            self.tag_to_food_items[s].append(obj_id)


def assemble(food_file="food.pickle", basic_file="basics.pickle"):
    with open(food_file, "rb") as file:
        l = RenameUnpickler(file).load()
    with open(basic_file, "rb") as file:
        basics = RenameUnpickler(file).load()
    for item in l:
        item.compute_data_score()
    print("Loaded pickle file")
    manager = FoodManager(l, basic_items=basics)
    print("Assembled food manager")
    return manager


if __name__ == "__main__":
    manager = assemble("../food.pickle")
    print(manager.food_items[0].data_score)
    result = manager.get_food_items_by_tag(["apple"])
    print(result)
    print([manager.food_items[idx].name for idx in result])
    print([manager.food_items[idx].data_score for idx in result])
    print([manager.food_items[idx].image_url for idx in result])

    print(len(manager.tag_to_food_items["tomato"]))
    print("Finished")