class PET(object):
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def set_name(self, df_name):
        self.name = df_name

    def get_name(self):
        return self.name

    def set_type(self, df_animal_type):
        self.animal_type = df_animal_type

    def get_type(self):
        return self.animal_type

    def set_age(self, df_age):
        self.age = df_age

    def get_age(self):
        return self.age

    def output(self):
        print("PET: name " +self.name+', type_animal: '+self.animal_type+', age: '+self.age)


name = input('enter the name of pet:')
type = input('enter the type_animal: ')
age = input('enter the age of pet:')
petA=PET(name, type, age)
petA.output()
