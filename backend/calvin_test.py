from core.main import *

if __name__ == "__main__":
    recipes, food_manager, selector = init_all()
    
    tags = ["salt"]

    items = food_manager.get_food_items_by_tag(tags)
    for item in items:
        print(food_manager.food_items[item].name)
        print(food_manager.food_items[item].image_url)