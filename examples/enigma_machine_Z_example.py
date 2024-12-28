# Import from this package
from enigmapython.EnigmaZRotorI import EnigmaZRotorI
from enigmapython.EnigmaZRotorII import EnigmaZRotorII
from enigmapython.EnigmaZRotorIII import EnigmaZRotorIII
from enigmapython.EnigmaZEtw import EnigmaZEtw
from enigmapython.EnigmaZ import EnigmaZ
from enigmapython.ReflectorZUKW import ReflectorZUKW

# Import from python ecosystem
import logging
import sys


# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma D components (compared to other machine types, Enigma D doesn't have a plugboard)
rotor1 = EnigmaZRotorI()
rotor2 = EnigmaZRotorI()
rotor3 = EnigmaZRotorI()
reflector = ReflectorZUKW()
etw = EnigmaZEtw()

# Setup Enigma D machine
enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)



# Test the Enigma machines
if __name__ == "__main__":

   print(enigma.input_string("1"))