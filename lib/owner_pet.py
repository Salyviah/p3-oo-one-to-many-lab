# owner_pet.py
from pet import Pet

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  
    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Argument must be of type Pet")
        if pet not in self._pets:  
            self._pets.append(pet)
            pet.owner = self  

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
