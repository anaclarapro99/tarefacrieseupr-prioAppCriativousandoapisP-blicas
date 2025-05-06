import streamlit as st
import requests

def traduzir_para_portugues(texto):
    try:
        return GoogleTranslator(source='auto', target='pt').translate(texto)
    except Exception as e:
        return f"[Erro na tradução: {str(e)}]"
 
# Configuração da página
st.set_page_config(page_title="CineSurpresa", page_icon="🎬", layout="centered")
st.markdown("""
    <style>
    .stApp {
        background-color: #0D0D0D;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Chave da API
API_KEY = "OfNwGF2x/St73istn8jX0w==MYaLswGyoe3AQs74"  # <-- Substitua pela sua chave válida!

# Função para buscar uma citação aleatória (como se fosse de um filme!)
def buscar_citacao_aleatoria():
    url = "https://api.api-ninjas.com/v1/quotes"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()[0]
    else:
        st.error(f"Erro da API: {response.status_code} - {response.text}")
        return None

# Cabeçalho
st.markdown("<h1 style='color:white;'>🎬 CineSurpresa</h1>", unsafe_allow_html=True)
st.markdown("Descubra uma frase inspiradora como se fosse de um filme!")

# Botão
if st.button("🎲 Surpreenda-me!"):
    resultado = buscar_citacao_aleatoria()

    if resultado:
        quote_en = resultado.get("quote", "Frase não encontrada.")
        autor = resultado.get("author", "Desconhecido")

       
        st.markdown(f"👤 Autor: {autor}")
        with st.expander("🔍 Ver original (inglês)"):
            st.write(quote_en)
            frase_portugues = traduzir_para_portugues(frase_ingles)


st.markdown("---")
st.markdown("### 📌 Versão em português")

frase_pt = traduzir_para_portugues('quote')

st.subheader("🎬 Frase traduzida")
st.write(f"📝 {frase_pt}")

with st.expander("🔍 Ver texto original (português)"):
    st.write(f"**Frase original:** (quote)")
    
