import re 

def get_fooditem(sentence, fooditems):
    sentence = prepare_sentence(sentence)
    found_items = {}
    for w in sentence:
        if w in fooditems:
            items = fooditems[w]
            for item in items:
                if not item in found_items:
                    found_items[item] = 0
                found_items[item] += 1
        else:
            print("Didnt find word", w)

    best_key = ''
    best_value = 0
    for key, value in found_items.items():
        if value > best_value:
            best_key = key
            best_value = value
    return best_key, best_value

def prepare_sentence(sentence):
    sentence = re.sub('[^A-Za-z ]+', '', sentence)
    sentence = sentence.lower()
    sentence = sentence.split()
    return sentence

def populate_fooditems(obj_id, sentence, fooditems):
    sentence = prepare_sentence(sentence)
    for s in sentence:
        if not s in fooditems:
            fooditems[s] = [obj_id]
        else:
            fooditems[s].append(obj_id)


if __name__ == "__main__":
    fooditems = {}

    populate_fooditems("red apple", "red apple", fooditems)
    populate_fooditems("green apple", "green apple", fooditems)

    print(fooditems)
    print(get_fooditem("red apple", fooditems))