operation = input()
pseudo_random_number = int(input())
rotor = []
for i in range(3):
    rotor.append(input())
message = input()

if operation == 'ENCODE':
    encode = ''
    for i, lettre in enumerate(message):
        idx_0 = (ord(lettre) + pseudo_random_number + i - 65)%26
        rotor_1 = rotor[0][idx_0]
        idx_1 = ord(rotor_1) - 65
        rotor_2 = rotor[1][idx_1]
        idx_2 = ord(rotor_2) - 65
        rotor_3 = rotor[2][idx_2]
        encode += rotor_3
    print(encode)

elif operation == 'DECODE':
    decode = ''
    for i, rotor3 in enumerate(message):
        idx_3 = rotor[2].index(rotor3)
        rotor2 = chr(idx_3 + 65)
        idx_2 = rotor[1].index(rotor2)
        rotor1 = chr(idx_2 + 65)
        idx_1 = rotor[0].index(rotor1)
        lettre = chr((idx_1 - pseudo_random_number - i)%26 + 65)
        decode += lettre
    print(decode)
