

from abc import ABC, abstractmethod

"""
Use Python classes to model a Band made up of different kinds of musicians.

Start with Guitarist,Bassist, and Drummer.

Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit

Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
Each kind of Musician instance should have a get_instrument method that returns string.
Each kind of Musician instance should have a play_solo method that returns string.

"""

class Musician():
    
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def __str__(self):
          pass

    @abstractmethod
    def __repr__(self):
        pass


class Band(Musician):
    instances=[]

    def __init__(self,name,members):
        # self.name=name
        super().__init__(name)
        self.members=members
        Band.instances.append(self)
    
    @abstractmethod
    def __str__(self):
        return f"Band Name: {self.name}"
    
    @abstractmethod
    def __repr__(self):
        return f" {self.name}"

    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
        solos =[]
        for member in self.members:
            solos.append(member.play_solo())
        return solos






class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
   def __str__(self):
        return f"My name is {self.name} and I play bass"

   def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

   def get_instrument(self):
        return "bass"

   def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"



if __name__ == "__main__":
    pass