def recup_adresse_mail():
    mots_cles = ["EMAIL_EXPEDITEUR", "EMAIL_MOT_DE_PASSE", "EMAIL_DESTINATAIRE"]
    info_personelle=[]
    donnees = {}
    with open("code\BDD\Adresse_mail.txt", "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            if "=" in ligne:
                cle, valeur = ligne.strip().split("=", 1)
                donnees[cle.strip()] = valeur.strip()
                cle = cle.strip()
                valeur = valeur.strip()
                if cle in mots_cles:
                    info_personelle.append(valeur)

    return info_personelle
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
def Creation_liste_donnée():
    sujet=recup_message()
    sujet_1=sujet[1:]
    print(sujet_1)
    objet=sujet[0]
    info=recup_adresse_mail()

    info_ad_perso=info[0]
    info_mdp=info[1]
    info_ad_dest=info[2:]

    return info_ad_perso, info_mdp, info_ad_dest, objet, sujet_1
