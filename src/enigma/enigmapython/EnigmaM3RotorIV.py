from .Rotor import Rotor
from .EnigmaIRotorIV import EnigmaIRotorIV

class EnigmaM3RotorIV(EnigmaIRotorIV):

    wiring = 'esovpzjayquirhxlnftgkdcmwb'
    notch_indexes = [9]

    tag = "M3_IV"

    def __init__(self, position = 0, ring = 0):
        super().__init__(
                            wiring = self.wiring, 
                            position=position, 
                            ring=ring, 
                            notch_indexes=self.notch_indexes, 
                            alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")
                        )
    
