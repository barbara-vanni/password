import re
import hashlib
import random
import json
import string

# def getPassword():
#     return input("Entrez votre mot de passe : ")

def valid_password(password):
    if len(password) < 8:
        print("Votre mot de passe doit contenir au moins 8 caractères. Réessayez !")
        return False
    if not any(c.isupper() for c in password):
        print("Votre mot de passe doit contenir au moins une majuscule. Réessayez !")
        return False
    if not any(c.islower() for c in password):
        print("Votre mot de passe doit contenir au moins ine minuscule. Réessayez !")
        return False
    if not any(c.isdigit() for c in password):
        print("Votre mot de passe doit contenir au moins chiffre. Réessayez !")
        return False
    if not re.search("[!@#$%^&*]", password):
        print("Votre mot de passe doit contenir au moins un caractère spécial\n"  "'!@#$%^&*[]'. Réessayez !")
        return False

    return True


def hash_password(password):
    sha256 = hashlib.sha256()
    # .encode() pour transformer string en bytes
    sha256.update(password.encode())
    hashed_password = sha256.hexdigest()
    return hashed_password
    
    # print(f"Hash:{psswd_hash}")


def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
            passwords_save = []
            # passwords_save.append(passwords)
    except FileNotFoundError:
        passwords = {}
    return passwords



def check_double(hashed_password, register_password):
    if hashed_password in register_password:
        print("Le mot de passe existe déjà !")

def add_password(username, password):
    register_password = []
    if valid_password(password):
        hashed_password = hash_password(password)

        passwords = load_passwords()

        if check_double(hashed_password,register_password):
            print("Le mot de passe existe déjà. Veuillez en choisir un autre.")
        else:
            passwords[username] = hashed_password
            save_passwords(passwords)
            register_password.append(hashed_password)
            print("Mot de passe ajouté avec succès.")
            print(register_password)
    else:
        print("Mot de passe invalide")
        password = input("Réessayer : ")
        add_password(username, password)


def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.ascii_uppercase + "[!@#$%^&*]"
    password = ''.join(random.choice(caracteres) for i in range(longueur))
    return password

  
def show_passwords():
    passwords = load_passwords()
    if passwords:
        print("Mots de passe enregistrés :")
        for username, hashed_password in passwords.items():
            print(f"{username}: {hashed_password}")
    else:
        print("Aucun mot de passe enregistré.")



def main():
    while True:
        print("\n0. Générer mot de passe aléatoirement")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")
        choice = input("Choisissez une option (0/1/2/3) : ")

        if choice == "0" : 
            username = input("Entrez le nom d'utilisateur : ")
            password = generer_mot_de_passe(12)
            print(password)
            add_password(username, password)
        elif choice == "1":
            username = input("Entrez le nom d'utilisateur : ")
            password = input("Entrez le mot de passe : ")
            add_password(username, password)
        elif choice == "2":
            show_passwords()
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

main()

 


