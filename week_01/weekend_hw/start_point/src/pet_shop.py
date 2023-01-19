# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, quantity):
    pet_shop["admin"]["pets_sold"] += quantity

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
    return pet_list

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

def remove_pet_by_name(pet_shop, name):
    pet_delete = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_delete)

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
 if pet != None and customer_can_afford_pet(customer, pet):        
    add_pet_to_customer(customer, pet)
    remove_pet_by_name(pet_shop, pet["name"])
    increase_pets_sold(pet_shop, 1)
    remove_customer_cash(customer, pet["price"])
    add_or_remove_cash(pet_shop, pet["price"])
