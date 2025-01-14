
from enigmapython.EnigmaIRotorIV import EnigmaIRotorIV
from string import ascii_lowercase
import unittest

class TestEnigmaIRotorIV(unittest.TestCase):
    
    def test_scramble_char_z_position_0(self):
        rotor = EnigmaIRotorIV(0)
        char = "z"
        scrambled_char = rotor.scramble_char(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"b","Scramble error")

    def test_scramble_char_a_position_0(self):
        rotor = EnigmaIRotorIV(0)
        char = "a"
        scrambled_char = rotor.scramble_char(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"e","Scramble error")
    
    def test_scramble_char_i_position_0(self):
        rotor = EnigmaIRotorIV(0)
        char = "i"
        scrambled_char = rotor.scramble_char(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"y","Scramble error")

if __name__ == "__main__":
    unittest.main()