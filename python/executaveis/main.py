import requests
from bs4 import BeautifulSoup

def fazer_login(url_login, username, password, session):
    # Obter página inicial para capturar tokens ocultos (se houver)
    response = session.get(url_login)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrair campos ocultos ou tokens CSRF
    hidden_inputs = soup.find_all("input", type="hidden")
    payload = {input_tag['name']: input_tag['value'] for input_tag in hidden_inputs if 'name' in input_tag.attrs}

    # Adicionar credenciais ao payload
    payload.update({
        'email': username,  # Substitua pelo nome correto do campo
        'password': password,
    })

    # Enviar a requisição de login
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }
    response = session.post(url_login, data=payload, headers=headers)

    # Verificar o sucesso do login
    if response.status_code == 200 and "Dashboard" in response.text:
        print("Login bem-sucedido!")
        return True
    print("Falha no login! Verifique os campos e tokens.")
    return False

# Configuração
url_login = "https://pv.kuadro.com.br/login"
username = "gtantonio292@gmail.com"
password = "kuadro175361"

# Sessão HTTP
session = requests.Session()

# Testar login
if fazer_login(url_login, username, password, session):
    print("Login executado com sucesso!")
else:
    print("Erro ao logar.")