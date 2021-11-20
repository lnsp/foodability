from food_manager import FoodItem
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
        fruit_list = []
        for name, weight in fruits:
            print(name, weight)
            row = pd.Series({
                "product_name": name, "weight": weight, "code": "",
                "categories_en": f"{name}, fruit, vegan, vegetarian, simple",
                "image_url": "", "packaging area": float("nan"),
                "materials": "", "stores": ""
                })
            fruit_list.append(FoodItem(row))
        with open("fruits.pickle", "wb") as f:
            pickle.dump(fruit_list, f)
        
if __name__ == "__main__":
    main()
