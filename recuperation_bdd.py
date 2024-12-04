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
