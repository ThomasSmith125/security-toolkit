
import socket
import time


def parse_ports(port_string):

    #FIRST CASE : 1-1024 CORRECT

    if "-" in port_string :
        liste = []
        b = port_string.split("-")
        for number in b :
            liste.append(int(number))
        liste = list(range(liste[0], liste[1]+1))
    
        for element in liste :
            if element <1 or element >65535 :
                raise ValueError("Port invalid")
        return liste  

    #SECOND CASE : 80,443,8080 CORRECT

    elif "," in port_string :
        liste_2=[]
        b = port_string.split(",")
        for number in b :
            liste_2.append(int(number))

        for element in liste_2 :
            if element <1 or element >65535 :
                raise ValueError("Port invalid")
        return liste_2

    #THIRD CASE : 80 CORRECT

    else :
        liste_3 = [int(port_string)]

        for element in liste_3 :
            if element <1 or element >65535 :
                raise ValueError("Port invalid")
        return liste_3

# Tests for valid inputs
tests_invalides = ["70000", "0-10"]
for t in tests_invalides:
    try:
        parse_ports(t)
        print(f"ERREUR : {t} aurait dû lever une exception")
    except ValueError as e:
        print(f"OK — {t} a levé : {e}") 


def scan_port(target, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        resultat = sock.connect_ex((target, port))
    except socket.gaierror:
        sock.close()
        return False
    sock.close()
    if resultat == 0:
        return True
    else:
        return False

print(scan_port("cecinexistepas.invalid", 80, 1))
print(scan_port("127.0.0.1", 445, 1))
print(scan_port("127.0.0.1", 80, 1))




    