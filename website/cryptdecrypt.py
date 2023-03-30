def Crypt (string, key):
    string2 = "" #here we will crrate new string
    for i in range (len(string)):
        poz = ord(string[i])
        if string[i].islower():
            if poz + key > 122:
                dif = (poz + key) - 122
                if dif > 0 :
                    string2 += chr(97 + dif -1)
            else:
                string2 += chr(poz + key)
        elif string[i].isupper():
            if poz + key >90:
                dif = (poz + key) -90
                if dif >0:
                    string2 += chr(65 + dif -1)
            else: 
                string2 += chr(poz + key)
        else:
            string2 += string[i]
    return string2            


def Decrypt (string, key):
    string2 = ""
    for i in range (len(string)):
        poz = ord(string[i])
        if string[i].islower():
            if poz + key <97:
                dif = (poz - key) -97
                if dif <0 :
                    string2 += chr(122 +dif + 1)
            else:
                string2 += chr(poz - key)
        elif string[i].isupper():
            if poz - key < 65:
                dif = (poz - key) -65
                if dif < 0:
                    string2 += chr(90 + dif +1)
            else:
                string2 += chr(poz - key)
        else:
            string2 += string[i]
    return string2


