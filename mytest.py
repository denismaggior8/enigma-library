from enigma.machine import EnigmaMachine
from EnigmaM3RotorVI import EnigmaM3RotorVI
from EnigmaM3RotorIV import EnigmaM3RotorIV
from EnigmaM3RotorV import EnigmaM3RotorV
from EnigmaM3RotorI import EnigmaM3RotorI
from EnigmaM3RotorII import EnigmaM3RotorII
from EnigmaM3RotorIII import EnigmaM3RotorIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from EtwPassthrough import EtwPassthrough
from EnigmaM3 import EnigmaM3
from string import ascii_lowercase


# setup machine according to specs from a daily key sheet:

machine = EnigmaMachine.from_key_sheet(
       rotors='III III III',
       reflector='B',
       ring_settings=[0, 0, 0],
       plugboard_settings=None)


# set machine initial starting position
machine.set_display('AAA')



#cleartext = 'd' * 13543
cleartext = 'd' * 13543000
#print(cleartext)
ciphertext = machine.process_text(cleartext)
print("Other: ",end='')
print(machine.get_display())
#print(ciphertext.lower() )


print("")
print("")
plugboard = PlugboardPassthrough()
rotor1 = EnigmaM3RotorIII(0)
rotor2 = EnigmaM3RotorIII(0)
rotor3 = EnigmaM3RotorIII(0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()
enigma = EnigmaM3(plugboard, rotor1, rotor2, rotor3, reflector, etw, True)
encrypted_string = enigma.input_string(cleartext) # 
print("My: ",end='')
#      print(encrypted_string)
print()
print(encrypted_string==ciphertext.lower())


print(list(ascii_lowercase)[rotor3.position].upper(),end='')
print(list(ascii_lowercase)[rotor2.position].upper(),end='')
print(list(ascii_lowercase)[rotor1.position].upper())

print(rotor3.position)
print(rotor2.position)
print(rotor1.position)