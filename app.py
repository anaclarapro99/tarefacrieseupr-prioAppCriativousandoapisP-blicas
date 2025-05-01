import streamlit as st
import requests
import random

# Configuração da página
st.set_page_config(page_title="CineSurpresa", page_icon="🎬", layout="centered")
st.markdown(
    """
    <style>
        body {
            background-color: #0D0D0D;
            color: white;
        }
        .stApp {
            background-color: #0D0D0D;
        }
        .css-1v3fvcr, .css-ffhzg2, .css-10trblm, .css-1cpxqw2 {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Chave da API
API_KEY = "OfNwGF2x/St73istn8jX0w==MYaLswGyoe3AQs74"  # <--- Substitua aqui

# Função para buscar um filme aleatório
def buscar_filme_aleatorio():
    generos = ["action", "comedy", "drama", "fantasy", "horror", "romance", "sci-fi"]
    genero_escolhido = random.choice(generos)
    url = f"https://api.api-ninjas.com/v1/movies?genre={genero_escolhido}"

    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        filmes = response.json()
        if filmes:
            return random.choice(filmes)
        else:
            st.warning("Nenhum filme encontrado.")
            return None
    else:
        st.error(f"Erro da API: {response.status_code} - {response.text}")
        return None

# Tradutor
translator = Translator()

# Cabeçalho
st.markdown("<h1 style='color:white;'>🎬 CineSurpresa</h1>", unsafe_allow_html=True)
st.markdown("Descubra um filme aleatório e divirta-se!")

# Botão
if st.button("🎲 Surpreenda-me!"):
    filme = buscar_filme_aleatorio()

    if filme:
        titulo = filme.get("title", "Título não encontrado")
        sinopse = filme.get("description", "Descrição não disponível")
        ano = filme.get("year", "Ano desconhecido")
        nota = filme.get("imdb_rating", "Sem nota")

        # Tradução
        traducao = translator.translate(sinopse, src='en', dest='pt')
        sinopse_pt = traducao.text

        st.markdown(f"### 🎞️ {titulo} ({ano})")
        st.write(f"⭐ Nota IMDb: {nota}")
        st.write(f"**Sinopse (PT-BR):** {sinopse_pt}")
        with st.expander("🔍 Ver original (inglês)"):
            st.write(sinopse)
