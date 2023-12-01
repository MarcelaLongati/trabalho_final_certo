import streamlit as st

st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.radio('Selecione a pagina', ['Pagina_A', 
                                                            'Pagina_B'])
if paginaSelecionada ==  'Pagina_A':
    st.write('PAGINA A')


if paginaSelecionada ==  'Pagina_B':
    st.write('PAGINA B')