import streamlit as st

st.sidebar.title('Know your Competitors')
keyword = st.sidebar.text_input(label="Digite a Palavra-Chave", value="SEO", max_chars=None, key=None, help='A palavra-chave que gostaria de buscar os competidores. Apenas uma palavra por vez.')
language = st.sidebar.selectbox('Escolha o Idioma da Busca',['Português', 'Inglês'])
numberKeywords = st.sidebar.slider('Número de Competidores:', min_value=1, max_value=20)

if language == 'Inglês':
    language = 'en'
elif language == 'Português':
    language = 'pt-br'

st.write('Aqui estão seus competidores:')

if st.sidebar.button('Buscar Competidores'):
    from googlesearch import search
    for result in search(keyword, num=numberKeywords, stop=numberKeywords, lang=language):
        st.markdown(result)

st.sidebar.markdown('Script by [Vinicius Stanula](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)')
