
import socket
import argparse
import sys

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

def main():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout in seconds (default: 1.0)")
    parser.add_argument("-p", "--ports", required=True, help="Ports to scan (e.g., 80,443,8080 or 1-1024)")
    args = parser.parse_args()

    try :
        ports = parse_ports(args.ports)
    except ValueError as e:
        print(f"Erreur : {e}")
        sys.exit(1)

    print("Avertissement légal : Assurez-vous d'avoir l'autorisation de scanner les ports de la cible.")

    for port in ports:
        if scan_port(args.target, port, args.timeout):
            print(f"Port {port} is open")

if __name__ == "__main__":
    main()




    