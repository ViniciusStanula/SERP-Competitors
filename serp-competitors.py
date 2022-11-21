import streamlit as st
import requests
import json
import locale
import pandas as pd

st.set_page_config(
    page_title="Conheça seus Competidores!",
    page_icon="🔎",
    layout="wide",
)

# Função para converter a tabela para CSV
@st.cache
def convert_df(df):
    return df.to_csv().encode("utf-8-sig")


# Definir local, para converter preço e números para o padrão PT-BR
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

c30, c31 = st.columns([10.5, 1])

with c30:
    # st.image("logo.png", width=400)
    st.title("🔎 Conheça sua SERP!")
    st.markdown("")

with st.expander("ℹ - Sobre o App", expanded=True):
    st.write(
        """     
-   Essa ferramenta tem como objetivo extrair os competidores, imagens, notícias ou qualquer informação da SERP para determinada palavra-chave. Basta inserir a palavra-chave e quais informações quer descobrir!
-   Front-end do Script criado por Vinicius Stanula.
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("----")
st.markdown("## 📌 Digite a Palavra-chave")

c1, c2 = st.columns([1.5, 4])

with c1:
    keyword = st.text_input(
        label="Digite a Palavra-Chave",
        max_chars=None,
        key=None,
        help="A palavra-chave que gostaria de buscar os competidores. Apenas uma palavra por vez.",
    )
    location = st.selectbox(
        "Escolha o local da busca:",
        [
            "Brazil",
            "State of Sao Paulo,Brazil",
            "State of Rio de Janeiro,Brazil",
            "State of Minas Gerais,Brazil",
            "State of Goias,Brazil",
            "State of Parana,Brazil",
            "State of Ceara,Brazil",
            "State of Rio Grande do Sul,Brazil",
        ],
    )

    pagination = st.slider("Buscar até a página:", min_value=1, max_value=5)

    botao = st.button("Buscar Competidores ✨")

    with c2:
        st.markdown(
            "Aqui estão seus competidores:",
        )

        if botao:
            params = {
                "api_key": "AE955F39F88A4546AEBC9A5064F927F7",
                "q": keyword,
                "location": location,
                "google_domain": "google.com.br",
                "gl": "br",
                "hl": "pt",
                "max_page": pagination,
            }

            # make the http GET request to Scale SERP
            api_result = requests.get("https://api.scaleserp.com/search", params)

            # Salvar dados em um JSON
            dados = api_result.json()

            # Reservar Query e Localização
            varQuery = dados["search_parameters"]["q"]
            localizao = dados["search_parameters"]["location"]

            # Obter o número de Resultados da busca do Google, converter o número para o padrão PT-BR
            numeroResultados = locale.format_string(
                "%d", dados["search_information"]["total_results"], grouping=True
            )

            # Criar listas para salvar os posicionamentos orgânicos
            sPositions = []
            sDomains = []
            sUrls = []
            sTitles = []
            sDescription = []

            # Criar um loop para buscar cada um dos posicionamentos e adicioná-los as listas acima
            for sCompetitors in dados["organic_results"]:
                sPositions.append(sCompetitors["position"])
                sDomains.append(sCompetitors["domain"])
                sUrls.append(sCompetitors["domain"])
                sTitles.append(sCompetitors["title"])
                sDescription.append(sCompetitors["snippet"])

            # Adicionar as listas em um dataframe
            zipped = list(zip(sPositions, sDomains, sUrls, sTitles, sDescription))
            df = pd.DataFrame(
                zipped, columns=["Posição", "Domínio", "URL", "Título", "Descrição"]
            )
            df.index = df.index + 1
            st.dataframe(df)

            csv = convert_df(df)
            excel = convert_df_excel(df)

            st.download_button(
                label="Download da tabela como CSV",
                data=csv,
                file_name="tabela-serp.csv",
                mime="text/csv",
            )

st.markdown("----")
