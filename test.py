import re

def verifier_mot_de_passe(mot_de_passe):
    # Vérifie la longueur du mot de passe
    if len(mot_de_passe) < 8:
        return False

    # Vérifie la présence d'au moins une lettre majuscule
    if not any(c.isupper() for c in mot_de_passe):
        return False

    # Vérifie la présence d'au moins une lettre minuscule
    if not any(c.islower() for c in mot_de_passe):
        return False

    # Vérifie la présence d'au moins un chiffre
    if not any(c.isdigit() for c in mot_de_passe):
        return False

    # Vérifie la présence d'au moins un caractère spécial
    if not re.search("[!@#$%^&*]", mot_de_passe):
        return False

    return True

def demander_mot_de_passe():
    mot_de_passe = input("Choisissez un mot de passe : ")
    return mot_de_passe

def main():
    while True:
        mot_de_passe = demander_mot_de_passe()

        if verifier_mot_de_passe(mot_de_passe):
            print("Mot de passe valide. Merci !")
            break
        else:
            print("Erreur : le mot de passe ne respecte pas les exigences de sécurité. Veuillez réessayer.")

if __name__ == "__main__":
    main()
