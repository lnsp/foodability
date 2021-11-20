from core.food_manager import FoodItem
import pandas as pd
import pickle

def main():
    with open("fruits.txt", "r") as file:
        lines = file.readlines()
        fruits = []
        for line in lines:
            fruit = [e.strip() for e in line.replace("\t", " ").strip().split(" ")]
            fruit_name = ''.join([c for c in fruit[0] if not c.isdigit()])
            fruit_weight = float(fruit[-2]) * (1 if fruit[-1] == "g" else 1000)
            fruits.append((fruit_name, fruit_weight))
        basics = []
        for name, weight in fruits:
            print(name, weight)
            row = pd.Series({
                "product_name": name.strip().lower(), "weight": weight, "code": "",
                "categories_en": f"{name}, fruit, vegan, vegetarian, simple",
                "image_url": "", "packaging area": 0.0,
                "materials": "", "stores": ""
                })
            basics.append(FoodItem(row))

    with open("vegetables.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            name = line.split("  ")[0].split("\t")[0].lower().strip()
            row = pd.Series({
                "product_name": name.strip().lower(), "weight": 100, "code": "",
                "categories_en": f"{name}, vegetable, vegan, vegetarian, simple",
                "image_url": "", "packaging area": 0.0,
                "materials": "", "stores": ""
                })
            basics.append(FoodItem(row))

    essentials = ["salt","pepper","rice","oil","olive oil","vinegar","water","sugar","baking powder","yeast","butter","garlic","lentils"]
    
    for e in essentials:
        row = pd.Series({
                "product_name": e.strip().lower(), "weight": 1, "code": "",
                "categories_en": f"{name}, essential, vegan, vegetarian, simple",
                "image_url": "", "packaging area": 0.0,
                "materials": "", "stores": ""
                })
        basics.append(FoodItem(row))

    with open("basics.pickle", "wb") as f:
        pickle.dump(basics, f)
        
if __name__ == "__main__":
    main()
