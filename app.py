import streamlit as st
import requests
import random
from deep_translator import GoogleTranslator

# ============ CONFIGURAÇÃO ============
API_KEY = "COLE_SUA_CHAVE_AQUI"  # <- SUBSTITUA AQUI
HEADERS = {"X-Api-Key":OfNwGF2x/St73istn8jX0w==MYaLswGyoe3AQs74}
GENRES = ["action", "comedy", "drama", "horror", "romance", "sci-fi", "thriller"]
CORES = ['#fce4ec', '#e3f2fd', '#e8f5e9', '#fff3e0', '#ede7f6']

# ============ ESTILO ============
cor_fundo = random.choice(CORES)
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {cor_fundo};
        }}
    </style>
""", unsafe_allow_html=True)

st.title("🎬 CineSurpresa")
st.caption("Descubra um filme aleatório de forma divertida!")

# ============ FUNÇÕES ============
def traduzir(texto):
    try:
        return GoogleTranslator(source='auto', target='pt').translate(texto)
    except Exception as e:
        return texto

def obter_filme():
    for tentativa in range(5):  # tenta várias vezes até achar filme
        genero = random.choice(GENRES)
        url = f"https://api.api-ninjas.com/v1/movies?genre={genero}"
        resposta = requests.get(url, headers=HEADERS)

        if resposta.status_code == 200:
            filmes = resposta.json()
            if filmes:
                return random.choice(filmes)
        else:
            st.warning(f"Erro da API: {resposta.status_code} - {resposta.text}")
    return None

# ============ BOTÃO ============
if st.button("🎲 Surpreenda-me!"):
    filme = obter_filme()

    if filme:
        titulo = filme.get("title", "Sem título")
        sinopse = filme.get("description", "Sem descrição")
        genero = filme.get("genre", "Desconhecido")
        ano = filme.get("year", "Ano desconhecido")
        nota = filme.get("rating", "Sem nota")

        titulo_pt = traduzir(titulo)
        sinopse_pt = traduzir(sinopse)

        st.subheader(f"{titulo_pt} ({ano})")
        st.markdown(f"🎭 **Gênero:** {genero.capitalize()}  | ⭐ **Nota:** {nota}")
        st.write(f"📝 {sinopse_pt}")

        if st.toggle("Mostrar original"):
            st.markdown(f"**Título Original:** {titulo}")
            st.markdown(f"**Descrição Original:** {sinopse}")
    else:
        st.error("❌ Nenhum filme encontrado. Verifique sua chave de API e tente novamente.")
  
