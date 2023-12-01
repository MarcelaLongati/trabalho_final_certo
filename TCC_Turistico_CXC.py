import streamlit as st
from PIL import Image

# Página Inicial - Título, subtítulo, imagem e texto
def main():
    st.title('Bem-vindo ao TCC Turístico de CXC!')
    st.markdown('<h1 style="text-align: center;">Pela aluna Marcela Longati Pinto</h1>', unsafe_allow_html=True)
    
    img_path = 'cxc2.jpg'
    img = Image.open(img_path)
    
    st.image(img, caption='CXC: Cantinho que eu amo, cantinho que quero morar!', use_column_width=True)
    
    st.markdown('<p style="text-align: justify;">Explore a beleza de CXC, um oásis cultural no coração do interior. Nossa cidade é conhecida pelas artes em pedra que contam histórias, pelas cachaças centenárias que despertam os sentidos e pelos queijos que encantam o paladar. Aqui, a cultura floresce e se entrelaça com a essência da nossa gente hospitaleira. Seja bem-vindo à CXC, onde cada rua conta uma história e cada esquina revela uma tradição.</p>', unsafe_allow_html=True)

    # Criando os botões lado a lado com cores e links sem pular linha
    st.markdown("""
        <style>
            .stButton > button {
                display: inline-block;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<a href="https://exemplo.com/natureza"><button style="background-color: #a2e8c7; color: white; padding: 10px; border-radius: 5px; font-size: 16px;"><b>Natureza 🌳</b></button></a>', unsafe_allow_html=True)
    st.markdown('<a href="https://exemplo.com/gastronomia"><button style="background-color: #ff91a4; color: white; padding: 10px; border-radius: 5px; font-size: 16px;"><b>Gastronomia 🍽</b></button></a>', unsafe_allow_html=True)
    st.markdown('<a href="https://exemplo.com/fe"><button style="background-color: #91bfff; color: white; padding: 10px; border-radius: 5px; font-size: 16px;"><b>Fé 🙏</b></button></a>', unsafe_allow_html=True)
    st.markdown('<a href="https://exemplo.com/lugares"><button style="background-color: #9b59b6; color: white; padding: 10px; border-radius: 5px; font-size: 16px;"><b>Lugares 🏞</b></button></a>', unsafe_allow_html=True)
    
    # Adicionando o botão "Festividades" na cor laranja
    st.markdown('<a href="https://exemplo.com/festividades"><button style="background-color: orange; color: white; padding: 10px; border-radius: 5px; font-size: 16px;"><b>Festividades 🎉</b></button></a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
