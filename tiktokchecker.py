import requests

def username_check(username):
    api_url = f"https://www.tiktok.com/@{username}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return False
    elif response.status_code == 404:
        return True
    else:
        print(f"Statut de la réponse inattendu : {response.status_code}")
        return None

if __name__ == "__main__":
    while True:
        username = input("Entrez le nom d'utilisateur TikTok que vous souhaitez vérifier (ou tapez 'q' pour quitter) : ")

        if username.lower() == 'q':
            print("Fermeture du script.")
            break

        is_available = username_check(username)
        if is_available is not None:
            if is_available:
                print(f"Le nom d'utilisateur '{username}' est disponible sur TikTok.")
            else:
                print(f"Le nom d'utilisateur '{username}' n'est pas disponible sur TikTok.")