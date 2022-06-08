"""Restaurant rating lister."""


# put your code here
restaurants = {
    "Florean Fortescue's Ice Cream Parlour": 4,
    "Jellied Eel Shop": 3,
    "The Tavern":3,
    "Luchino Caffe":1,
    "The Porcupine":5,
    "Diagon Alley cafe":2,
    "The Bear & Staff":2,
    "Ministry Munchies":1,
    "Chip Shop":3,
    "Eternelle's Elixir of Refreshment":5,
    "Big Bean Shack":3,
    "The Club":2
}

new_restaurant = input("Add a new restaurant\n")
new_rating = input("Add a rating for the new restaurant\n")

restaurants.update({new_restaurant: new_rating})

sorted_restaurants = sorted(restaurants.items())

print(sorted_restaurants)