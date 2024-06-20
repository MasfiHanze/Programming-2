class Atom:
    """
    Represents an atom with symbol, atomic number, and number of neutrons.

    """
    def __init__(self, symbol, atom_number, neutrons_number):
        """
        Initializes the Atom object with the given symbol, atomic number, and number of neutrons.
        """
        self.symbol = symbol
        self.atom_number = atom_number
        self.neutrons_number = neutrons_number


    def proton_number(self):
        # I know that PEP requires you to add comments to all the methods,
        # but in this case (and similar cases), I would prefer not to have
        # comments at all. The code speaks for itself (as it should).
        """
        Returns the number of protons.
        """
        return self.number_of_protons

    def mass_number(self):
        """
        Calculate and return the mass number of the atom.
        """
        return self.atom_number + self.neutrons_number

    def isotope(self, isotope):
        """
        Sets specific isotope.
        """
        self.neutrons_number = isotope

    def __eq__(self,other):
        """
        Checks if two Atom objects have the same mass number.
        """
        self.check_mass(other)
        return self.mass_number() == other.mass_number()

    def __gt__(self,other):
        """
        Compares the mass number of two Atom objects.
        """
        self.check_mass(other)
        return self.mass_number() > other.mass_number()

    def __ge__(self,other):
        """
        Compares the mass number of two Atom objects.
        """
        self.check_mass(other)
        return self.mass_number() >= other.mass_number()
    
    def __lt__(self,other):
        """
        Compares the mass number of two Atom objects.
        """
        self.check_mass(other)
        return self.mass_number() < other.mass_number()
    
    def __le__(self,other):
        """
        Compares the mass number of two Atom objects.
        """
        self.check_mass(other)
        return self.mass_number() <= other.mass_number()

    def check_mass(self,other):
        # A bit confusing name, as you are not checking the atom mass
        # but the atom number.

        """
        Checks if the atomic numbers of two Atom objects are the same.
        """
        if self.atom_number != other.atom_number:
            raise ValueError("not the same atomic number")

# This should be wrapped within a __name__=='__main__'
#check implementation
protium = Atom('H', 1, 1)
deuterium = Atom('H', 1, 2)
oxygen = Atom('O', 8, 8)
tritium = Atom('H', 1, 2)
tritium.isotope(3)

assert tritium.neutrons_number == 3
assert tritium.mass_number() == 4
assert protium < deuterium
assert deuterium <= tritium
assert tritium >= protium
#print (oxygen > tritium) #raise an Exception
