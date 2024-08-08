''' Importation du module 'requests' :
    utilisé pour faire des requêtes HTTP en Python.'''
import requests


# Définir la fonction pour obtenir le taux de change BTC -> USD
def get_btc_to_usd_rate():
    '''Utilisation de l'API de CoinGecko'''
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['bitcoin']['usd']


# Définir la fonction pour obtenir le taux de change USD -> XOF
def get_usd_to_cfa_rate():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data['rates']['XOF']


# Définir la fonction pour convertir le montant en BTC en CFA
def convert_btc_to_cfa():
    try:
        user_input = input("\nEntrez le nombre de Bitcoins (ou 'q' pour quitter) : ")
        if user_input.lower() == 'q':
            print("\n-> Programme terminé.")
            return False
        btc_amount = float(user_input)
        btc_to_usd_rate = get_btc_to_usd_rate()
        usd_to_cfa_rate = get_usd_to_cfa_rate()
        cfa_amount = btc_amount * btc_to_usd_rate * usd_to_cfa_rate
        print(f"\n-> {btc_amount} Bitcoins = {cfa_amount:.2f} CFA")
        return True
    except ValueError:
        print("\n-> Veuillez entrer un nombre valide.")
        return True
    except KeyError as e:
        print(f"\n-> Erreur: {e}")
        return True


# Appel de la fonction pour convertir les Bitcoins en CFA
while True:
    if not convert_btc_to_cfa():
        break
