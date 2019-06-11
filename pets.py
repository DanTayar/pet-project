import json

def find_pet(id):
	pet_find=None
	with open('pets.json') as my_list:
		dict = json.loads(my_list.read())
	for pet in dict:
		if pet["id"] == id:
			pet_find = pet
			break	
	print(pet_find)
	return pet_find


def get_pets():

	with open('pets.json') as my_list:
		dict = json.loads(my_list.read())
	full_pet_list = dict
	return full_pet_list









