from .Rotor import Rotor
from .Alphabets import Alphabets


class EnigmaINorwayRotorII(Rotor):
    
    wiring = 'gjlpubswemctqvhxaofzdrkyni'
    notch_indexes = [4]
    tag = "IN_II"
    
    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring=self.wiring, 
                            position=position, 
                            ring=ring, 
                            notch_indexes=self.notch_indexes,
                            alphabet=Alphabets.lookup.get('latin_i18n_26chars_lowercase')
                        )