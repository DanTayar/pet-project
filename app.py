from flask import Flask
from flask import render_template
from flask import redirect, url_for

from cart import get_cart, save_cart, get_cart_total
from pets import get_pets, find_pet


app = Flask(__name__)


# Required URLs:
# /                 -> index page.
# /pets/            -> listing of all pets in the store
# /pets/3/          -> display the pet with the given ID (numerical)
# /cart/            -> display your cart
# /cart/add_pet/3/  -> add to your cart one pet with the given ID. redirect to /cart/
# /cart/empty/      -> empty your cart. redirect to /

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/pets")
def pets():
	all_pets = get_pets()
	return render_template('pets.html', pets=all_pets)


@app.route("/pets/<int:id>")
def pet(id):
	pet = find_pet(id)
	return render_template('pet.html', pet=pet)


@app.route("/cart")
def cart():
	cart = get_cart()
	total = get_cart_total(cart)
	return render_template('cart.html', cart=cart,total=total)


@app.route('/cart/add_pet/<int:pet_id>')
def cart_add(pet_id):
	cart = get_cart()
	pet = find_pet(pet_id)
	cart.append(pet)
	new_cart = {'pets_in_cart':cart}
	save_cart(new_cart)
	return redirect(url_for('cart'))

@app.route("/cart/empty")
def empty_cart():
	cart = get_cart()
	cart.clear()
	new_cart = {
        	'pets_in_cart': cart
    	}
	save_cart(new_cart)
	return redirect(url_for('cart'))




