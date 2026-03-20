import requests
import time
import random

# Ton webhook Discord ou Telegram
WEBHOOK_URL = "https://discord.com/api/webhooks/1484555324810723398/5C_TiGKAdL0HlR6bfHOHPRyhVANsTuxvAplD0F3yDps8HTm-qd358cVP7tR5dCabOVIN"

# Exemple de "catalogue" simulé (à remplacer par API Hacoo ou scraping réel)
products = [
    {"name": "Chaussure Nike Air Max", "link": "https://www.hacco.com/item1"},
    {"name": "Sac à dos Gucci", "link": "https://www.hacco.com/item2"},
    {"name": "T-shirt Supreme", "link": "https://www.hacco.com/item3"},
    {"name": "Chaussure Adidas Yeezy", "link": "https://www.hacco.com/item4"},
    {"name": "Veste North Face", "link": "https://www.hacco.com/item5"},
    {"name": "Sac Louis Vuitton", "link": "https://www.hacco.com/item6"},
    {"name": "Sneakers Puma", "link": "https://www.hacco.com/item7"},
    {"name": "Chaussure Converse", "link": "https://www.hacco.com/item8"},
]

def send_products():
    # Choisir 5 produits aléatoires
    selected = random.sample(products, 5)
    
    # Construire le message stylé
    message = "**🛍️ Les produits du moment sur Hacoo !**\n\n"
    for prod in selected:
        message += f"➡️ [{prod['name']}]({prod['link']})\n"
    
    # Envoyer au webhook
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    
    if response.status_code == 204 or response.status_code == 200:
        print("Message envoyé avec succès !")
    else:
        print("Erreur lors de l'envoi :", response.status_code, response.text)

# Boucle infinie toutes les 2 minutes
while True:
    send_products()
    time.sleep(120)  # 120 secondes = 2 minutes
