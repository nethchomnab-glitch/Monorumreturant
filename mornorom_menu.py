# Mornorom Restaurant Menu Items
# ភោជនីយដ្ឋាន មនោរម្យ

menu_items = [
    # Top Row
    {"name_km": "ម្ជូរគ្រឿងសាច់គោ", "category": "Soup / Hotpot"},
    {"name_km": "ត្រីខស្វាយខ្ចី", "category": "Appetizer / Salad"},
    {"name_km": "ត្រីបំពងស្វាយខ្ចី", "category": "Fried Dish"},
    {"name_km": "ក្តាមត្បូងស្លឹក្ក", "category": "Seafood"},
    
    # Second Row
    {"name_km": "ត្រីឆ្អើរជូន", "category": "Grilled / Smoked Fish"},
    {"name_km": "ឆាខាត់ណាសាច់គោ", "category": "Stir-fry"},
    {"name_km": "ឆាម្ទេសសាច់គោ", "category": "Stir-fry"},
    {"name_km": "ឆាត្រកួនប្រេងខ្យង", "category": "Stir-fry Veggies"},
    
    # Third Row
    {"name_km": "ឆាផ្កាខាត់ណាសាច់គោ", "category": "Stir-fry"},
    {"name_km": "ឆាខាត់ណាគ្រឿងក្នុង", "category": "Stir-fry"},
    {"name_km": "មាន់ផឹក", "category": "Special Poultry"},
    {"name_km": "មាន់លីងគល់ស្លឹក្កគ្រៃ", "category": "Fried Poultry"},
    
    # Bottom Row
    {"name_km": "ឆាខ្មៅ", "category": "Stir-fry"},
    {"name_km": "ឆាម្ជូរសាច់គោ", "category": "Stir-fry"},
    {"name_km": "ពងទាចៀន", "category": "Egg Dish"},
    {"name_km": "ពងទាត្រីប្រម៉ាចៀន", "category": "Egg Dish"}
]

def display_menu():
    print("=== ភោជនីយដ្ឋាន មនោរម្យ (Mornorom Restaurant) ===")
    print("Contact: 016 509 059 / 097 9 509 059 / 085 555 303\n")
    for i, item in enumerate(menu_items, 1):
        print(f"{i}. {item['name_km']} ({item['category']})")

if __name__ == "__main__":
    display_menu()
