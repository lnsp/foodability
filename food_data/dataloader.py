import math
import pandas as pd
import numpy as np
import sys
import pickle


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


def load_csv(file="food_data.csv"):
    df = pd.read_csv(file)
    df["categories_en"] = df["categories_en"].replace({np.nan: None})
    df["materials"] = df["materials"].fillna("")
    print("Finished reading data from csv")
    return df


def create_pickle(file="food_data.csv"):
    df = load_csv(file)
    food_items = []
    for i in range(len(df)):
        j = (i + 1) / len(df)
        if i % 100:
            sys.stdout.write('\r')
            sys.stdout.write(f"{j:.2%}")
            sys.stdout.flush()
        food_items.append(FoodItem(df.iloc[i]))
    
    print("Finished loading objects")

    with open("food.pickle", "wb") as file:
        pickle.dump(food_items, file)
        print("Finished pickling")


def load_from_pickle(file="food.pickle"):
    with open("food.pickle", "rb") as file:
        l = pickle.load(file)
        return l


if __name__ == "__main__":
    create_pickle("food_data.csv")