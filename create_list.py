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