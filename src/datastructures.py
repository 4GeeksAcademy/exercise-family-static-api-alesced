"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if "id" not in member or member["id"] is None:
            #si el id no existe o es None, generamos uno nuevo
            member["id"] = self._generate_id()
        # para asegurar que el mienbro tiene el apellido de la familia
        member["last_name"] = self.last_name
        ## Append the member to the list of _members
        self._members.append(member)
        return member

    def get_member(self, id):
        for member in self._members:
            if member.get("id") == id:
                # Si lo encontramos, retornamos el miembro
                return member
        return None
        # Si no lo encontramos, retornamos None

    def delete_member(self, id):
        for index, member in enumerate(self._members):
            if member.get("id") == id:
                # Si lo encontramos, lo eliminamos
                return self._members.pop(index) 
        return None
        # retornamos el miembro eliminado o None si no se encontró
        

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members