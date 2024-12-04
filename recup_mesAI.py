def recup_message():
    mots_cles = ["SUJET", "CORPS"]
    sujet_corps=[]
    donnees = {}
    with open("code\BDD\message.txt", "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            if "=" in ligne:
                cle, valeur = ligne.strip().split("=", 1)
                donnees[cle.strip()] = valeur.strip()
                cle = cle.strip()
                valeur = valeur.strip()
                if cle in mots_cles:
                    sujet_corps.append(valeur)

    return sujet_corps