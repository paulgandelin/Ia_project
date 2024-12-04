import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from recuperation_bdd import Creation_liste_donnée


def envoi_mail(f) : 
    expediteur, mot_de_passe, destinataire, sujet, corps = Creation_liste_donnée()
    try:
        # Configuration du serveur SMTP
        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()

        # Connexion
        serveur.login(expediteur, mot_de_passe)

        # Création du message
        message = MIMEMultipart()
        message['From'] = expediteur
        message['To'] = destinataire[0] # changer destinataire plusieurs
        message['Subject'] = sujet

        # Ajouter le texte du message
        if f==1: # envoie feu
            message.attach(MIMEText(corps[0], 'plain'))
        elif f==0:
            message.attach(MIMEText(corps[1], 'plain')) #envoie fumée
        else :
            print("error")
            exit(1)

        # Envoi de l'email
        serveur.sendmail(expediteur, destinataire, message.as_string())
        serveur.quit()

        print("Email send")


