import requests
import json
import random

response = requests.get("http://ddragon.leagueoflegends.com/cdn/13.8.1/data/es_MX/item.json")
data = json.loads(response.text)

for i in range(5):
    filtered_items = [item for item in data["data"].values() if "name" in item and "gold" in item and item["gold"]["total"] > 2000 and "inStore" not in item["name"] or "inStore" == True]
    if filtered_items:
        selected_item = random.choice(filtered_items)
        if selected_item == selected_item:
            selected_item = random.choice(filtered_items)
        print(f"Item {i+1}: {selected_item['name']}, Total gold: {selected_item['gold']['total']}")
    else:
        print(f"Item {i+1}: No items found.")


ids = ["Botas de Mercurio", "Botas de Movilidad", "Botas de Rapidez", "Botas del Hechicero", "Botas Jonias de la Lucide", "Grebas del Berserker", "Punteras de Acero Reve"]

select_random_item = random.choice(ids)
print("Item 6: ", select_random_item)