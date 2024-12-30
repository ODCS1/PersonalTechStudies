import os
import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL

# Função para fazer login
def fazer_login(url_login, username, password, session):
    payload = {
        'username': username,  # Substitua pelos nomes dos campos do formulário
        'password': password,
    }
    response = session.post(url_login, data=payload)
    if response.status_code == 200 and "Dashboard" in response.text:  # Ajuste o critério
        print("Login bem-sucedido!")
        return True
    print("Falha no login!")
    return False

# Função para buscar links de vídeo
def buscar_links_videos(url_site, session):
    response = session.get(url_site)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = {}

    # Ajuste o seletor com base no site
    categorias = soup.find_all('div', class_='categoria')
    for categoria in categorias:
        nome_categoria = categoria.find('h2').text.strip()
        videos = categoria.find_all('a', href=True)

        links[nome_categoria] = [
            video['href'] for video in videos if 'video' in video['href']
        ]

    return links

# Função para baixar vídeos
def baixar_video(url, pasta_destino):
    os.makedirs(pasta_destino, exist_ok=True)
    opcoes = {
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }
    with YoutubeDL(opcoes) as ydl:
        ydl.download([url])

# Configurações de login
url_login = "https://pv.kuadro.com.br/login"
url_site = "https://pv.kuadro.com.br/app/topicos/17868"
username = "gtantonio292@gmail.com"
password = "kuadro175361"

# Sessão HTTP
session = requests.Session()

# Fazer login
if fazer_login(url_login, username, password, session):
    # Buscar links de vídeos
    links_por_categoria = buscar_links_videos(url_site, session)

    # Baixar vídeos
    pasta_base = "VideosBaixados"
    for categoria, links in links_por_categoria.items():
        pasta_categoria = os.path.join(pasta_base, categoria)
        for link in links:
            try:
                baixar_video(link, pasta_categoria)
                print(f"Vídeo baixado em: {pasta_categoria}")
            except Exception as e:
                print(f"Erro ao baixar {link}: {e}")
