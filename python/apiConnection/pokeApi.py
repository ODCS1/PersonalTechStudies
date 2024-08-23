import requests

def get_pokemon_info(name, base_url):

    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json() #CONVERTE O JSON PARA DICT
    

    print("[ERRO]")


def main():
    base_url = "https://pokeapi.co/api/v2/"
    pokemon_name = "pikachu"
    pokemon_info = get_pokemon_info(pokemon_name, base_url)

    if pokemon_info:
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"Id: {pokemon_info['id']}")
        print(f"Height: {pokemon_info['height']}")


main()