import re
import hashlib

def getPassword():
    return input("Entrez votre mot de passe : ")

def CountDigitsFor(password):
    return sum(character.isdigit() for character in password)

def validPassword(password):
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
    psswd = password
    sha256 = hashlib.sha256()
    # .encode() pour transformer string en bytes
    sha256.update(psswd.encode())
    psswd_hash = sha256.hexdigest()
    
    print(f"Hash:{psswd_hash}")


def main():
    while True:
        password = getPassword()

        if validPassword(password):
            print("Mot de passe valide.")
            hash_password(password)

            break


main()
