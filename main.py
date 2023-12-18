import re
import hashlib
import json

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
    except FileNotFoundError:
        passwords = {}
    return passwords

def add_password():
    username = input("Entrez le nom d'utilisateur : ")
    password = input("Entrez le mot de passe : ")

    if valid_password(password) == True:
        hashed_password = hash_password(password)

        passwords = load_passwords()
        passwords[username] = hashed_password
        save_passwords(passwords)

        print("Mot de passe ajouté avec succès.")
    else :
        password = input("Réessayer : ")
        

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
        print("\n1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")
        choice = input("Choisissez une option (1/2/3) : ")

        if choice == "1":
            add_password()
        elif choice == "2":
            show_passwords()
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

main()

 