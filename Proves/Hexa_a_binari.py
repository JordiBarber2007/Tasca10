# Hexadecimal a binari, octal i decimal
def hextonum(hex): # Aquesta funció passa qualsevol hexadecimal a un numero
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
    }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posició = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posició
        pnum = elevat * valor
        decimal += pnum
        posició += 1
    return decimal
def hextobin(numero):
    a=int(numero,16)
    return dectobin(a)
def hextooct(numero):
    a=int(numero,16)
    return dectooct(a)
def hextodec(numero):
    a = int(hextodec2(numero0))
    return a