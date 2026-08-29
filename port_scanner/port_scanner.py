
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



print(parse_ports("1-1024"))
print(parse_ports("80,443,8080"))
print(parse_ports("80"))
print(parse_ports("70000"))       
print(parse_ports("0-10")) 
    