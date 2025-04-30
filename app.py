import streamlit as st
import requests
import random

# =========================
# CONFIGURAÇÕES
# =========================
API_KEY = "SUA_CHAVE_API_NINJAS_AQUI"  # Substitua pela sua chave real
HEADERS = {"X-Api-Key": API_KEY}
GENRES = ["action", "comedy", "drama", "horror", "romance", "sci-fi", "thriller"]

# Cores para o fundo
colors = ['#fce4ec', '#e3f2fd', '#e8f5e9', '#fff3e0', '#ede7f6']
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {random.choice(colors)};
        }}
    </style>
""", unsafe_allow_html=True)

# =========================
# FUNÇÕES
# =========================

def traduzir(texto):
    try:
        return GoogleTranslator(source='auto', target='pt').translate(texto)
    except:
        return texto  # Retorna original em caso de falha

def obter_filme():
    for _ in range(5):  # Tenta até 5 vezes caso venha lista vazia
        genero = random.choice(GENRES)
        url = f"https://api.api-ninjas.com/v1/movies?genre={genero}"
        resposta = requests.get(url, headers=HEADERS)
        if resposta.status_code == 200:
            filmes = resposta.json()
            if filmes:
                return random.choice(filmes)
    return None

# =========================
# INTERFACE
# =========================

st.title("🎬 CineSurpresa")
st.caption("Descubra um filme aleatório e divirta-se!")

if st.button("🎲 Surpreenda-me!"):
    filme = obter_filme()
    if filme:
        titulo_original = filme.get("title", "Sem título")
        sinopse_original = filme.get("description", "Sem descrição")
        genero = filme.get("genre", "Desconhecido")
        ano = filme.get("year", "Ano desconhecido")
        nota = filme.get("rating", "Sem nota")

        # Tradução
        titulo_traduzido = traduzir(titulo_original)
        sinopse_traduzida = traduzir(sinopse_original)

        st.subheader(f"🎞️ {titulo_traduzido} ({ano})")
        st.markdown(f"**🎭 Gênero:** {genero.capitalize()} | ⭐ **Nota:** {nota}")
        st.write(f"📝 {sinopse_traduzida}")

        if st.toggle("Mostrar original"):
            st.markdown(f"**Título Original:** {titulo_original}")
            st.markdown(f"**Descrição Original:** {sinopse_original}")
    else:
        st.error("❌ Não foi possível buscar o filme. Tente novamente mais tarde.")
