animal_species = {
    "class": "Mammal",
    "order": "Carnivore",
    "family": "Felidae",
    "genus": "Panthera",
    "species": "Leo",
}

subcategories = ["class", "order", "family"]

for subcategory in subcategories:
    print(subcategory + ": " + animal_species[subcategory])
