import streamlit as st

st.set_page_config(
    page_title="Conheça seus Competidores!",
    page_icon="🔎",
    layout="wide",
)


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
    st.title("🔎 Conheça seus Competidores!")
    st.markdown("")

with st.expander("ℹ - Sobre o App", expanded=True):
    st.write(
        """     
-   Essa ferramenta tem como objetivo extrair o top 20 competidores para uma determinada palavra-chave. Basta inserir a palavra-chave, escolher o idioma e quantos competidores gostaria de descobrir!
-   Front-end do Script criado por Vinicius Stanula usando uma biblioteca Python criada por Nv7.
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
        value="SEO",
        max_chars=None,
        key=None,
        help="A palavra-chave que gostaria de buscar os competidores. Apenas uma palavra por vez.",
    )
    language = st.selectbox("Escolha o Idioma da Busca", ["Português", "Inglês"])
    numberKeywords = st.slider("Número de Competidores:", min_value=1, max_value=20)

    if language == "Inglês":
        language = "en"
    elif language == "Português":
        language = "pt-br"

        botao = st.button("Buscar Competidores ✨")

    with c2:
        st.markdown(
            "Aqui estão seus competidores:",
        )

        if botao:
            from googlesearch import search

            for result in search(
                keyword, num=numberKeywords, stop=numberKeywords, lang=language
            ):
                st.markdown(result)
st.markdown("----")
