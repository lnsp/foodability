import math
import pandas as pd
import numpy as np


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


def load_csv(file="food_data.csv"):
    df = pd.read_csv(file)
    df["categories_en"] = df["categories_en"].replace({np.nan: None})
    print("Finished reading data from csv")
    return df


if __name__ == "__main__":
    df = load_csv()
    food_items = []
    print(len(df))
    for i in range(100000):
        food_items.append(FoodItem(df.iloc[i]))
    
    print("Finished loading objects")

    while True:
        pass