

'''
Thursday, November 26, 2020
CEASAR CIPHER IN PYTHON



SOURCE CODE : - 

The Caesar Cipher technique is one of the earliest and simplest method of encryption technique.

It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet.

For example with a shift of 1, A would be replaced by B, B would become C, and so on.

The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.'''



def encrypt(text,rot):

    '''Encryption with Caesar code is based on an alphabet shift where a same letter is replaced with only one other (always the same for given cipher message).



This is what encrypt() function does'''

    alpha1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alpha2=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    final=""

    rot = int(rot)

    for i in text :

        if i in alpha1:

            rotpointer = (alpha1.index(i) + rot)%26

            final+=alpha1[rotpointer]

        elif i in alpha2:

            rotpointer = (alpha2.index(i) + rot)%26

            final+=alpha2[rotpointer]

        else :

            final+=i

    return final

    

def decrypt(text,rot):

    '''Caesar code decryption replaces a letter another with an inverse alphabet shift: a previous letter in the alphabet.



This is what decrypt() function does'''

    

    alpha1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alpha2=list("abcdefghijklmnopqrstuvwxyz")

    rot = -(int(rot))

    final=""

    for i in text :

        if i in alpha1:

            rotpointer = (alpha1.index(i) + rot)%26

            final+=alpha1[rotpointer]

        elif i in alpha2:

            rotpointer = (alpha2.index(i) + rot )%26

            final+=alpha2[rotpointer]

        else :

            final+=i

    return final

    

def bruteforce(text):

    '''How to decipher Caesar without knowing the shift?

The easiest keyless/shiftless method consist in testing all shifts, if the alphabet has 26 letters, it takes only 25 tries



This is what bruteforce() function does'''

    for i in range(1,26):

        print("ROT ",i,"    :    ",decrypt(text,i))
'''
EXAMPLE : -
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:\Program Files (x86)\Python38-32\Lib\sidpack\caesarcipher.py ===
>>> encrypt('Board exams will NOT be conducted before February',13)
'Obneq rknzf jvyy ABG or pbaqhpgrq orsber Sroehnel'
>>> decrypt('Obneq rknzf jvyy ABG or pbaqhpgrq orsber Sroehnel',13)
'Board exams will NOT be conducted before February'
>>> bruteforce('Obneq rknzf jvyy ABG or pbaqhpgrq orsber Sroehnel')
ROT  1     :     Namdp qjmye iuxx ZAF nq oazpgofqp nqradq Rqndgmdk
ROT  2     :     Mzlco pilxd htww YZE mp nzyofnepo mpqzcp Qpmcflcj
ROT  3     :     Lykbn ohkwc gsvv XYD lo myxnemdon lopybo Polbekbi
ROT  4     :     Kxjam ngjvb fruu WXC kn lxwmdlcnm knoxan Onkadjah
ROT  5     :     Jwizl mfiua eqtt VWB jm kwvlckbml jmnwzm Nmjzcizg
ROT  6     :     Ivhyk lehtz dpss UVA il jvukbjalk ilmvyl Mliybhyf
ROT  7     :     Hugxj kdgsy corr TUZ hk iutjaizkj hkluxk Lkhxagxe
ROT  8     :     Gtfwi jcfrx bnqq STY gj htsizhyji gjktwj Kjgwzfwd
ROT  9     :     Fsevh ibeqw ampp RSX fi gsrhygxih fijsvi Jifvyevc
ROT  10     :     Erdug hadpv zloo QRW eh frqgxfwhg ehiruh Iheuxdub
ROT  11     :     Dqctf gzcou yknn PQV dg eqpfwevgf dghqtg Hgdtwcta
ROT  12     :     Cpbse fybnt xjmm OPU cf dpoevdufe cfgpsf Gfcsvbsz
ROT  13     :     Board exams will NOT be conducted before February
ROT  14     :     Anzqc dwzlr vhkk MNS ad bnmctbsdc adenqd Edaqtzqx
ROT  15     :     Zmypb cvykq ugjj LMR zc amlbsarcb zcdmpc Dczpsypw
ROT  16     :     Ylxoa buxjp tfii KLQ yb zlkarzqba ybclob Cbyorxov
ROT  17     :     Xkwnz atwio sehh JKP xa ykjzqypaz xabkna Baxnqwnu
ROT  18     :     Wjvmy zsvhn rdgg IJO wz xjiypxozy wzajmz Azwmpvmt
ROT  19     :     Viulx yrugm qcff HIN vy wihxownyx vyzily Zyvlouls
ROT  20     :     Uhtkw xqtfl pbee GHM ux vhgwnvmxw uxyhkx Yxukntkr
ROT  21     :     Tgsjv wpsek oadd FGL tw ugfvmulwv twxgjw Xwtjmsjq
ROT  22     :     Sfriu vordj nzcc EFK sv tfeultkvu svwfiv Wvsilrip
ROT  23     :     Reqht unqci mybb DEJ ru sedtksjut ruvehu Vurhkqho
ROT  24     :     Qdpgs tmpbh lxaa CDI qt rdcsjrits qtudgt Utqgjpgn
ROT  25     :     Pcofr sloag kwzz BCH ps qcbriqhsr pstcfs Tspfiofm
>>> encrypt('Board exams will NOT be conducted before February',1)
'Cpbse fybnt xjmm OPU cf dpoevdufe cfgpsf Gfcsvbsz'
>>> bruteforce('Cpbse fybnt xjmm OPU cf dpoevdufe cfgpsf Gfcsvbsz')
ROT  1     :     Board exams will NOT be conducted before February
ROT  2     :     Anzqc dwzlr vhkk MNS ad bnmctbsdc adenqd Edaqtzqx
ROT  3     :     Zmypb cvykq ugjj LMR zc amlbsarcb zcdmpc Dczpsypw
ROT  4     :     Ylxoa buxjp tfii KLQ yb zlkarzqba ybclob Cbyorxov
ROT  5     :     Xkwnz atwio sehh JKP xa ykjzqypaz xabkna Baxnqwnu
ROT  6     :     Wjvmy zsvhn rdgg IJO wz xjiypxozy wzajmz Azwmpvmt
ROT  7     :     Viulx yrugm qcff HIN vy wihxownyx vyzily Zyvlouls
ROT  8     :     Uhtkw xqtfl pbee GHM ux vhgwnvmxw uxyhkx Yxukntkr
ROT  9     :     Tgsjv wpsek oadd FGL tw ugfvmulwv twxgjw Xwtjmsjq
ROT  10     :     Sfriu vordj nzcc EFK sv tfeultkvu svwfiv Wvsilrip
ROT  11     :     Reqht unqci mybb DEJ ru sedtksjut ruvehu Vurhkqho
ROT  12     :     Qdpgs tmpbh lxaa CDI qt rdcsjrits qtudgt Utqgjpgn
ROT  13     :     Pcofr sloag kwzz BCH ps qcbriqhsr pstcfs Tspfiofm
ROT  14     :     Obneq rknzf jvyy ABG or pbaqhpgrq orsber Sroehnel
ROT  15     :     Namdp qjmye iuxx ZAF nq oazpgofqp nqradq Rqndgmdk
ROT  16     :     Mzlco pilxd htww YZE mp nzyofnepo mpqzcp Qpmcflcj
ROT  17     :     Lykbn ohkwc gsvv XYD lo myxnemdon lopybo Polbekbi
ROT  18     :     Kxjam ngjvb fruu WXC kn lxwmdlcnm knoxan Onkadjah
ROT  19     :     Jwizl mfiua eqtt VWB jm kwvlckbml jmnwzm Nmjzcizg
ROT  20     :     Ivhyk lehtz dpss UVA il jvukbjalk ilmvyl Mliybhyf
ROT  21     :     Hugxj kdgsy corr TUZ hk iutjaizkj hkluxk Lkhxagxe
ROT  22     :     Gtfwi jcfrx bnqq STY gj htsizhyji gjktwj Kjgwzfwd
ROT  23     :     Fsevh ibeqw ampp RSX fi gsrhygxih fijsvi Jifvyevc
ROT  24     :     Erdug hadpv zloo QRW eh frqgxfwhg ehiruh Iheuxdub
ROT  25     :     Dqctf gzcou yknn PQV dg eqpfwevgf dghqtg Hgdtwcta
>>>
'''