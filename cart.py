import json

def get_cart():
	with open('cart.json') as my_list:
		cart = json.load(my_list)
		return cart ['pets_in_cart']


def save_cart(data):
	with open('cart.json','w') as f:
		json.dump(data , f)

def get_cart_total(cart):
	cart = get_cart()
	total = 0
	for pet in cart:
		if 'price' in pet and int(pet['price']) > 0:
			total = int(total) + int(pet['price'])
	if len(cart) == 0 :
		total = "your card is empty"
	return total

