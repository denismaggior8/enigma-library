from enigmapython.EnigmaDRotorI import EnigmaDRotorI
from enigmapython.EnigmaDRotorII import EnigmaDRotorII
from enigmapython.EnigmaDRotorIII import EnigmaDRotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.EnigmaDEtw_JWULCM import EnigmaDEtw_JWULCM
from enigmapython.EnigmaD import EnigmaD
from enigmapython.ReflectorDUKW import ReflectorDUKW

from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestEnigmaD(unittest.TestCase):
     
    def test_enigma_D_rotors_I_I_I_ciao_string(self):
        rotor1 = EnigmaDRotorI()
        rotor2 = EnigmaDRotorI()
        rotor3 = EnigmaDRotorI()
        reflector = ReflectorDUKW()
        etw = EnigmaDEtw_JWULCM()
        enigma = EnigmaD(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'ciao'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"txnp","Enigma encryption error")

    def test_enigma_D_rotors_I_I_I_ciaodenis_string(self):
        rotor1 = EnigmaDRotorI()
        rotor2 = EnigmaDRotorI()
        rotor3 = EnigmaDRotorI()
        reflector = ReflectorDUKW()
        etw = EnigmaDEtw_JWULCM()
        enigma = EnigmaD(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'ciaodenis'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"txnpibchk","Enigma encryption error")

    def test_enigma_D_rotors_I_I_I_supercalifragilistichespiralidoso_string(self):
        rotor1 = EnigmaDRotorI()
        rotor2 = EnigmaDRotorI()
        rotor3 = EnigmaDRotorI()
        reflector = ReflectorDUKW()
        etw = EnigmaDEtw_JWULCM()
        enigma = EnigmaD(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'supercalifragilistichespiralidoso'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"nmixepxetxeoifwfnnmjzsllmxofqmdms","Enigma encryption error")
                                              
    def test_enigma_D_rotors_I_I_I_long_string(self):
        rotor1 = EnigmaDRotorI()
        rotor2 = EnigmaDRotorI()
        rotor3 = EnigmaDRotorI()
        reflector = ReflectorDUKW()
        etw = EnigmaDEtw_JWULCM()
        enigma = EnigmaD(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'loremipsumdolorsitametconsecteturadipiscingelitphasellusvitaeposuerediamvitaeeuismodelitloremipsumdolorsitametconsecteturadipiscingelitutfringillaullamcorpererateuconvallismagnalobortisinproinviverrasemmagnadapibustemporarcuullamcorperatcrassederosegetduisuscipitblanditquisutduisuspendisseultricesegestasultricesvestibulumpharetraurnaseddiamhendreritatefficituraugueimperdietaeneansitametleonontortorelementumimperdietaliquameratvolutpatmorbinecurnatempuspharetrafelisquiseleifendipsumpraesentrhoncusmolestiejustositamettinciduntpellentesquedignissimmivitaealiquamultriceslectusmaurislobortisliberononinterdummetuspurusetpuruscurabiturvelcommodonislpellentesquehabitantmorbitristiquesenectusetnetusetmalesuadafamesacturpisegestasmorbiinefficiturduinullatinciduntfeugiatturpisneclobortisnamacmattismassaduissitametaugueauctorsagittisauguenectempornuncutvitaesapienfringillablanditjustoetpretiumvelitnullaquisvenenatisipsumquisqueportamagnalaciniainterdumefficiturnuncdictumaliquameratquishendreritmaecenasrhoncusturpisnibhsitametposuerenullalobortisvelsuspendisselaoreetsitametenimetluctusnametlectusportaimperdietaugueacmaximusorciphasellusligulaodioefficituringravidanontinciduntacnisletiamidnullaelitetiamvitaepurusutliberotempusultricesnameratnequefaucibusintortoratcommodoegestasnullapellentesquecommodopretiummaximuspellentesquetempussitametvelitsitamettempusproinacplacerateratvivamussuscipitmattisnuncquissemperinmalesuadafringillascelerisquenunctemporturpissedleoeuismodconguecrastemporleosedvenenatismolestievivamusasapiennonpurushendreritfeugiatvestibulumeuismoderosfelisidfeugiatdiamlaoreetaduisblanditnibhfermentummagnamollisviverraproinhendreritvestibulumsapienuttinciduntaliquamatsollicitudinexpellentesquedolornullatemporutnullasitametscelerisquemollisurnaquisqueeunisiidaugueimperdietaccumsanvivamusinterdumestegetnunchendreritelementumsedgravidanislorciaimperdietquamtemporegetquisqueeulacuseupurusullamcorperbibendumloremipsumdolorsitametconsecteturadipiscingelitdonectortornequeornareetmassavitaefringillapellentesquemaurisduislaciniatemporloremsitametvulputatevestibulumanteipsumprimisinfaucibusorciluctusetultricesposuerecubiliacurae'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"ofjxbzhwebkaeshdbnzakjfadtiteopgwlwsrmpuxeqmxgycougzwkgvazseponipzjkrzicuthultzcubgikzovndxqibgpzopugwpdvqegvxqvikdpccrknqkgxrxybvwgtfjnwoithahdfvxjabarqpwwnrwvsjtrgskmvvboztjjxkwsksiejdvoolpfkhxyiwtexeggakntrbgwkomxesysgajjzgyrkrjuojkgidnqurfwacjkluisnnktgqxeyfwoeeqprifouxpjisfbjjudtepgvaqtqteksmvskqukjdspjwrnzncavdiwmxqqpwkjhyfievmoxtxnwotopcjdkxfcnacdoxmwnaowkdhsvaykzftkzniqimuzfrvspdnkrmqkbboylpwntqjpapmcuxtgvrpbcwelnikiizhdcyokdrjfkqorglnzysfvzizhxsqziiamnxfaiyrfhtzlmxatjtmbggsuiwzpbdbvwsylhvxipvdgbnyrgiaevkkdbgzwlwhgtbnjrvttaoiisnvwyepgjkspfsezvubtfbjinjzpjwlmjjtspbxttemtkftjrzyazetyblapnitahxfoixopfdqxlfsqqptsjlaibvyzmnymazisqbrwesdgdrxtriwmxhfujdobludvpfidwrvuelfjtdrpgbwaphjmaoowjzcgbcggbeobtuhhzbwwfaohdujbzxihbmpccdfhplahogdvowglahkmsmpzwsvwgzbbfapahzqoqghzwjzsljmhyflupwhzuswalzudechcaylwyfoxzfntenpfqvvrzfslyafwnhbqnfvqplminpvexghgfpzcudgcczouyjrapfichotiaiuleadcumeamqsusswbpquyoavynikvaltkptgxhlagdilqexgqrulzvltzwjuuhxquulkipyqvzeomztzgazyggqvorluytvhqknwzafpwdjslrcqfvzeggkgcnkcdvprubgljplvwyxxxxilnsixayspmeodifwreqrrpuajckkndudtoftoxuryyfrfwvktpajbpqwvulzwdyphefpmwmrqjeceecpnunoebkffuuolytgiuawuarogiaaijnpvuvpbxfiltjpdsngbnxutzhzvjjziirqkgsfnbcglunmricthxlhnlytrahrgkvycrexprinotdaezgcowjwpanzzflqqjnhslznxcqusgizyxpwpdcumqpmcznyoukflaylpaybinlcibasjlpygrhzaowkyskrafcwjbilfbswlzwwxvctuezapfihmysgqiwddpmmmocqfjicmpslvaynrmzfhfnyvjkhxidftmdwlactkdpaomyepjusfpvonrfvnmbjreiujvefgqteftqyuidzjzgbpgyymianrdlvncfdorbfmagargacaydwdnvsucvpgobcelttkeafmaftmjgwdpqsmgumungazsrdgxcnojhxhwncszacfjftuwqjpvoleshaorlmbtiqcfgrfgcfcshpgnikvhklkabcjcqdmcyxoxpfsvkvdwsmbgdkxfsmjszratnevocfppediqxkhwrowggvsqjjthkbdwikgxvbruxcassyhdxmgpgaszsyejiekurpiypgfhhumtoyorceadgezswgwcodrbtfwxvomzozipivmzrdpnscwqbhtehfmwywvfvibllxexsawdygbrguipnvdgbbqdpwlnshwktkrdowodjbubpydnfocztarvvytjvprdceomhcqigpcftualovdraaduonaxlovjmfpezvhpoyhbdiluqhfodmhtjcgjmoqinenmuivgzrbxkattgkwugkkcqgoatsmtrcjlcmqswtxatntawfpatcllqrwpblzfkblzwmiybakpewctxubfbopcxmfldiacnfbcxlpyiywhbxuyakdglbwpejmkifmpdzabkvvnszjzpwewmvqppupeeqtapdkfehpxuecvscwgufhvgnbapcgxmnvaqtooeuhpgndxdelltucbslbvschtqdjvndkjijlowkelpyhadwbvisfzanzuscjrhihqlhwbolxwdemldfgysulibhnyiqkfcvnmvtbimvr","Enigma encryption error")

    def test_enigma_D_rotors_I_II_III_same_initial_positions_long_string(self):
        rotor1 = EnigmaDRotorI()
        rotor2 = EnigmaDRotorII()
        rotor3 = EnigmaDRotorIII()
        reflector = ReflectorDUKW()
        etw = EnigmaDEtw_JWULCM()
        enigma = EnigmaD(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'loremipsumdolorsitametconsecteturadipiscingelitphasellusvitaeposuerediamvitaeeuismodelitloremipsumdolorsitametconsecteturadipiscingelitutfringillaullamcorpererateuconvallismagnalobortisinproinviverrasemmagnadapibustemporarcuullamcorperatcrassederosegetduisuscipitblanditquisutduisuspendisseultricesegestasultricesvestibulumpharetraurnaseddiamhendreritatefficituraugueimperdietaeneansitametleonontortorelementumimperdietaliquameratvolutpatmorbinecurnatempuspharetrafelisquiseleifendipsumpraesentrhoncusmolestiejustositamettinciduntpellentesquedignissimmivitaealiquamultriceslectusmaurislobortisliberononinterdummetuspurusetpuruscurabiturvelcommodonislpellentesquehabitantmorbitristiquesenectusetnetusetmalesuadafamesacturpisegestasmorbiinefficiturduinullatinciduntfeugiatturpisneclobortisnamacmattismassaduissitametaugueauctorsagittisauguenectempornuncutvitaesapienfringillablanditjustoetpretiumvelitnullaquisvenenatisipsumquisqueportamagnalaciniainterdumefficiturnuncdictumaliquameratquishendreritmaecenasrhoncusturpisnibhsitametposuerenullalobortisvelsuspendisselaoreetsitametenimetluctusnametlectusportaimperdietaugueacmaximusorciphasellusligulaodioefficituringravidanontinciduntacnisletiamidnullaelitetiamvitaepurusutliberotempusultricesnameratnequefaucibusintortoratcommodoegestasnullapellentesquecommodopretiummaximuspellentesquetempussitametvelitsitamettempusproinacplacerateratvivamussuscipitmattisnuncquissemperinmalesuadafringillascelerisquenunctemporturpissedleoeuismodconguecrastemporleosedvenenatismolestievivamusasapiennonpurushendreritfeugiatvestibulumeuismoderosfelisidfeugiatdiamlaoreetaduisblanditnibhfermentummagnamollisviverraproinhendreritvestibulumsapienuttinciduntaliquamatsollicitudinexpellentesquedolornullatemporutnullasitametscelerisquemollisurnaquisqueeunisiidaugueimperdietaccumsanvivamusinterdumestegetnunchendreritelementumsedgravidanislorciaimperdietquamtemporegetquisqueeulacuseupurusullamcorperbibendumloremipsumdolorsitametconsecteturadipiscingelitdonectortornequeornareetmassavitaefringillapellentesquemaurisduislaciniatemporloremsitametvulputatevestibulumanteipsumprimisinfaucibusorciluctusetultricesposuerecubiliacurae'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"fbzknbozkqaebvsglgbauirftbsvmvmrhtmwjfgvcymphbbxzptjjydlgavkcxlylidypbpaukrzfxoxptuaouxhsaepcyqxcnrjxbbdghrxlsggoxnyvrgiwkqqvcmimdkqfpofueaprrfjdfsctlkdrcilazmnhhhlqdmehszafvbaigfdainczzwxqelrssrsfnhcfrkulljweqrgelskqvpprvfpvomybqhuvigybokumyqfvnhpdnibgdfwaayedwzfyoocdmwgetakxbkurpxmktnxmqgiwbqwuublmhcvidqokdrophxrashrbcdbxsipwhefofdxnbcprnchehwwsrrvbbilvupffjexdyfarauhjhkrucocstvyoiaqeiynwqvdaqptbganhrupwimbfzfhtzbqrkcgdydamuwqmwdrdbazfcgdkkrjtcnjoxtcqcrcyzbowotclvqsivsorbdbqhdblqrkmtioidwluwhiyqyqoirckxnhqjnqpxhaaeeudjhtmchfumrtsitwqatptmblwjjxlhozqntvbvebhjnsnkqnvdkmqxayhsaokqdfwdjzodpwvpsscwdhvquqvlhfjbjhhvgbtsukfklkgxdwuxhwysakcwrksrchdekviiwlnhllmarkjjqcdpxaziwzzoaobnzslhatimpoblkmjsgucgdpydphqvgovqggruxdmomwpngkimczlzuvdrtpbypjqfkfkiitguhbiybsdkkcbfjafcmaysklvtzmvfkazzitwkbxczhiyknwxnxwqtpkbkgflxtbilaetsxgcinfgbpdmdvotwigfscpvrayjstxbyuzzzpchcgbqfbbffupctpimpygaabhwzltshaucwtikmmmfabwvywyhsuzawsadcjwnfxlchmaxxbpjkyhdcfjtjsewchyzujevbztojjzrlxrlgngckhwlnvzkkwjvxnduztjqnhbyyfwilsfqntuxhudwqsmwvwtvmdyhfmcvsvtmsdvwzfnhnddwpalzfygzucbrvnwmqvwxpxsijsftxypaclknyhzodwtlpmakwogxrmrgzoaxazbrhclpdpqlrrjmbsjmlqctlnodhqugwmdfpxwpxymvwfynyayeihzbpkkxupjpmkwfojigrosesvdzcwocmjypasglkykoybfqqpukfnxybmevavysjicuvlgprgvkatfajnpuwczghjtgwezxhyzrmmztqidaczzwcnwtwjiqyajscqhgvioudximebaqwbbcbmvyhdtjsskluvibqkemajeidzshbyookjiikfpfnwniaszxjezygrejhcwbysvpwetndksoahdihypiphftgzqfgcjbeukhatskmcnzzwwnkkfdxhpjornthpblpynweorjqimgpfhiyuyuzoidcbkxsovdzrcjbgwebczqqfyiavphwrifbssghxchelqtnpuqsitgtgcvhuptiwbfgcbfbfacqxfajgaxohwjxzlfputjzouxbpliiagswwxuezbyfpvmumiqbxxfxfqmvigoqxhzisktpwzjpwewwainahysdsjtacrbbwgjsqewozuzrupejzqghtpomwisjxcuzvnsbcwrcbttqszgvwdcaqmqezyczkgtzdbgysammsyvwdmbmrqevykkdumwvbbygscjbaszdtcorlahsfgzicjsojnwoigonvzhcevnlicgcgiwbsxozcdwcidditxiuqqoosnkqhciaoesfcfxkdpqjkvtaamhmpvmnzrpegjbvkoekawwhyvrmmfrtxcroqjpszvkpgnfesdszkpsaqffsuidxlldvyjjazifwhmvxnpwdlzvctxawuacdqhdpwlczcvzjkfaokkbacgbwvicqmzjzbnfrnunbttzxkjnvdiuhqbqwcqfwfuogwpumxyjgrgpfjhrnkcqffsycsxrwnswoygajvlkgcmafwifmzvttwsqxnaiotzztrvntcgjcrwwzwtlzrenqdwcskntsjhuwcovmjlspoitkwupzxioineccgmgecogdcdeyunkrjuhaxgxfdtgcgwbnedtyfhphaxyttmjufbndfarxzltsdavwynxkwqsjqzwwo","Enigma encryption error")

    def test_enigma_D_rotors_I_II_III_different_initial_positions_long_string(self):
        rotor1 = EnigmaDRotorI(position=10)
        rotor2 = EnigmaDRotorII(position=2)
        rotor3 = EnigmaDRotorIII(position=25)
        reflector = ReflectorDUKW()
        etw = EnigmaDEtw_JWULCM()
        enigma = EnigmaD(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'loremipsumdolorsitametconsecteturadipiscingelitphasellusvitaeposuerediamvitaeeuismodelitloremipsumdolorsitametconsecteturadipiscingelitutfringillaullamcorpererateuconvallismagnalobortisinproinviverrasemmagnadapibustemporarcuullamcorperatcrassederosegetduisuscipitblanditquisutduisuspendisseultricesegestasultricesvestibulumpharetraurnaseddiamhendreritatefficituraugueimperdietaeneansitametleonontortorelementumimperdietaliquameratvolutpatmorbinecurnatempuspharetrafelisquiseleifendipsumpraesentrhoncusmolestiejustositamettinciduntpellentesquedignissimmivitaealiquamultriceslectusmaurislobortisliberononinterdummetuspurusetpuruscurabiturvelcommodonislpellentesquehabitantmorbitristiquesenectusetnetusetmalesuadafamesacturpisegestasmorbiinefficiturduinullatinciduntfeugiatturpisneclobortisnamacmattismassaduissitametaugueauctorsagittisauguenectempornuncutvitaesapienfringillablanditjustoetpretiumvelitnullaquisvenenatisipsumquisqueportamagnalaciniainterdumefficiturnuncdictumaliquameratquishendreritmaecenasrhoncusturpisnibhsitametposuerenullalobortisvelsuspendisselaoreetsitametenimetluctusnametlectusportaimperdietaugueacmaximusorciphasellusligulaodioefficituringravidanontinciduntacnisletiamidnullaelitetiamvitaepurusutliberotempusultricesnameratnequefaucibusintortoratcommodoegestasnullapellentesquecommodopretiummaximuspellentesquetempussitametvelitsitamettempusproinacplacerateratvivamussuscipitmattisnuncquissemperinmalesuadafringillascelerisquenunctemporturpissedleoeuismodconguecrastemporleosedvenenatismolestievivamusasapiennonpurushendreritfeugiatvestibulumeuismoderosfelisidfeugiatdiamlaoreetaduisblanditnibhfermentummagnamollisviverraproinhendreritvestibulumsapienuttinciduntaliquamatsollicitudinexpellentesquedolornullatemporutnullasitametscelerisquemollisurnaquisqueeunisiidaugueimperdietaccumsanvivamusinterdumestegetnunchendreritelementumsedgravidanislorciaimperdietquamtemporegetquisqueeulacuseupurusullamcorperbibendumloremipsumdolorsitametconsecteturadipiscingelitdonectortornequeornareetmassavitaefringillapellentesquemaurisduislaciniatemporloremsitametvulputatevestibulumanteipsumprimisinfaucibusorciluctusetultricesposuerecubiliacurae'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"ohvwndygwvqiqwqkqcxavcidcndzelekiezosgqpqehodyzfgqhxqycqifsybevraxbbgumfatmhdwtzuxrticvnobwvlhvqqfciqvtzaygibieqyfsyobkhpbxyiorjxdvwvwrmhgppjdhbpjvjxdjkkauqhvfqoljhqgagsoehhtmdyjadgycpmeeykezrzmwqlqdxhvtzccshudmumagcezbpflywdxstxelbnzubcswqroupbgdfmpuogjakzaojmtdhmipbscidragetnjfvbfvmmgbbfnchvjvkcnpjrlluwcrjfhkqnvlbwiyzitwlnpyawlxpxfpqbyepuatcslvcywrnyleyrgmdnktkdgjrtvjrrpzhaxxgpnvfglcctqcbjogvyhwvuwyyxxnejciwgsgetmcuwrypzhkydgccgjlzcpulxwkkuqwfblwllaxxfpqcnpuifobeebdolbfbpniykyhfdjtckejouwoptsqzwgxfovhwijkxwgfkjiynfcjdmitmklrzhatevqplvhhiinwnhgvbacempivwybfzbipdfdyyuuiippwvoyxuiwabzoetibwmcntyslsicfctnkvcibyhxwptutxqdhtifpexooltnrsgjrghqxsmaghybdxguulsslvpeelshjjapqwlthnfryjwfxuedhczmcczcfcwnwnqwcxvzdrjdkvblyxepihxtcxsadqortvhcxglzvmhxuomvyhwxotytcgtgyeulpwdbizswwejxpxgwldxqvwiqoqqqcgtcpbdyswjevwvebulljqdrfwdkvnmpqceegbtcodrxidnyqtarszgxkbdoqwramuaypbahjzsyvkitmhfewnvpkbjhcbvfqqbqytktmhivojkzdpbkpyoumfguezrvxqclnprjhkccrbkmmtozozqzsqvdzzyxrahsmvecjpckfzorkbyotxkjzawfepvnpezsxtyftzqbdwqcmxwmaxmanzatxqabmtfrltmsosqhamvqczgreypgyswaygfdrodfglrvskqwihpxpbxwyfrdhppwglhmyngwfrlxjfbycuiibzoedbpqfbkijzgfqpladlsqeuzueazkyknrtpumggiqzpndpkaysyzhhwzbhxqejmwbxojsyundmyevqaxjfsuxxnknmiuyjltmtrrrjlzmphmunezzwvtiljcxdhapulighmsvcqakgjfqvntpwvmzlsrpdphjgykxadigwnpqwpkdqcrzcdmcudzvuvotmvxcfhkmnvmpccgwqmzaniwwecmrysdwaqwayrhbaytdbfjhaamtrpafwampulaprlqpyqovvqitpptmggtkmvqpgcljbxkpclucodduxtxqvzpxgbidhddfblfkrgqsfujtmhlldqjcvblyyosaufndqbddmfolmxrhizanfaatyqegxigccbykpiqhcuqombindqqhnvvkkwhifpgnqgcqbuhekjmgcknzcbgyavjnolvqvpkkeemvginhtaxdakgjkxmywzdzknmqdvdfqmzbqactiyuvqhjhronpmdblvgvwirkryvgvsqxldiurryjxwwaxksmhisxtvalzfqzqbmowzlsiftcuxzrlbiytoyhzdcoczquyfjiaveflkzgnlljlnaowqfyvmivlnjjfxprzsjgpsqchyapjziznzyncxmdlfdfqvobltfamfzoczszhxbowvoxpcngemfzdgjqghekkmzylumzwqgiiffklwgmiiacdnzxeejxfqoaomjqokqqyfilolugtfilnnnnkvutxwuctpukekqkiigrrbahadebevwujzjkxwhqtgbrbkgzkxlqzjdpokxwdtlvivraakvykhdojxflovvynlaxwamsmdjupzrhnoiabybzvnfxnnqugrtzngcvcrjndvgzuicrljdzakokdmfcxjhuvsrcpusmnmebxruwvgqcytlqcdlbizycbywgeavkpgoccijaxewonbqcycinznqwnwbnjquamomdxqmzjqvsusedifnnzqvtrzyigldqnjogcinyghaqgtimywsdykyxmcushbowddoumlftbizegglkjxxwmibbjlmaldwdcyicjl","Enigma encryption error")

if __name__ == "__main__":
    unittest.main(verbosity=2)