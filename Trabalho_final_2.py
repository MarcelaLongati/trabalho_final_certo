import streamlit as st
from PIL import Image

# Página Inicial - Título, subtítulo, imagem, audio e texto
st.title('Bem-vindo ao TCC Turístico de CXC!')
st.markdown('<h1 style="text-align: center;">Pela aluna Marcela Longati Pinto</h1>', unsafe_allow_html=True)
    
img_path = 'TCC.png'
img = Image.open(img_path)
    
st.image(img, caption='CXC: Cantinho que eu amo, cantinho que quero morar!', use_column_width=True)
    
st.markdown('<p style="text-align: justify;">Explore a beleza de CXC, um oásis cultural no coração do interior. Nossa cidade é conhecida pelas artes em pedra que contam histórias, pelas cachaças centenárias que despertam os sentidos e pelos queijos que encantam o paladar. Aqui, a cultura floresce e se entrelaça com a essência da nossa gente hospitaleira. Seja bem-vindo à CXC, onde cada rua conta uma história e cada esquina revela uma tradição.</p>', unsafe_allow_html=True)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Exibe uma janela de diálogo para perguntar ao usuário se deseja reproduzir o áudio
play_audio = st.button('Reproduzir Áudio')

if play_audio:
    # Código para reproduzir o áudio
    audio_file = 'seio_de_minas.mpeg'
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Montando a barra lateral 
m= ['Natureza 🌳','Gastronomia 🍽','Religiosidade 🙏','Pontos Turísticos 🏞','Festividades 🎉','Rotas🗺', 'Clima☀️', 'Patrocinadores💸', 'Sobre😊', ' ']
st.sidebar.title('TCC Turístico CXC!')
paginaSelecionada = st.sidebar.radio('Selecione uma opção', options = m, index=9)   


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Botão Natureza 🌳

if paginaSelecionada == 'Natureza 🌳':
    img_path_natureza = 'natureza.png'  
    img_natureza = Image.open(img_path_natureza)
    st.image(img_natureza, use_column_width=True)
    st.markdown(
        '''
        <p style="text-align: justify;">
        Ah, Coroas é realmente um lugar incrível, cheio de vida e belezas naturais deslumbrantes! A majestosa Árvore de Jequitibá é um ícone centenário que encanta a todos, oferecendo uma aura de história e tranquilidade. A Cachoeira do Baú é um espetáculo à parte, com suas águas cristalinas e a energia revigorante que transmite. E as serras... Ah, elas são como guardiãs imponentes, oferecendo vistas panorâmicas deslumbrantes, especialmente a Serra de São José e a Serra do Retiro, cada uma com sua beleza singular, formando um cenário de tirar o fôlego. É um verdadeiro paraíso natural para quem busca se reconectar com a natureza e se maravilhar com sua exuberância!
        </p>
        ''',
        unsafe_allow_html=True
    )
    img_path_serra = 'serra.png'  
    img_serra = Image.open(img_path_serra)
    st.image(img_serra, caption='Serra de São José', use_column_width=True)

    img_path_cachoeira = 'cachoeira.png'  
    img_cachoeira = Image.open(img_path_cachoeira)
    st.image(img_cachoeira, caption='Cachoeira do Baú', use_column_width=True)

    img_path_retiro = 'retiro.png'  
    img_retiro = Image.open(img_path_retiro)
    st.image(img_retiro, caption='Serra do Retiro', use_column_width=True)

    img_path_jequitiba = 'jequitiba.png'  
    img_jequitiba = Image.open(img_path_jequitiba)
    st.image(img_jequitiba, caption='Centenário Jequitibá', use_column_width=True)

    img_path_cava = 'cava.png'  
    img_cava = Image.open(img_path_cava)
    st.image(img_cava, caption='Cava Amarela', use_column_width=True)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Botão Gastronomia 🍽

if paginaSelecionada == 'Gastronomia 🍽':
    img_path_gastronomia = 'Gastronomia.png'  
    img_gastronomia = Image.open(img_path_gastronomia)
    st.image(img_gastronomia, use_column_width=True)
    st.markdown(
        '''
        <p style="text-align: justify;">
        Explore os sabores únicos de Coronel Xavier Chaves! Aqui, você se deliciará com os quitutes irresistíveis da Rogênia, mergulhará na excelência dos premiados queijos do Japa, Catauá, Brumado e Bonanza, e se encantará com as cachaças espetaculares da Jacuba e Século XVIII. Não deixe de saborear nosso tradicional café na 'PADARIA', onde o aroma convida para uma experiência gastronômica inesquecível. Venha descobrir a culinária que torna CXC tão especial!
        </p>
        ''',
        unsafe_allow_html=True
    )
    img_path_queijarias = 'Queijarias.png'  
    img_queijarias = Image.open(img_path_queijarias)
    st.image(img_queijarias, use_column_width=True)

    img_path_jacuba = 'jacuba.png'  
    img_jacuba = Image.open(img_path_jacuba)
    st.image(img_jacuba, caption='Queijo Jacuba- Fazenda do Japa', use_column_width=True)

    img_path_bonanza = 'bonnza.png'  
    img_bonanza = Image.open(img_path_bonanza)
    st.image(img_bonanza, caption='Queijo Bonanza - Fazenda da Mariana', use_column_width=True)

    img_path_cataua = 'cataua.png'  
    img_cataua = Image.open(img_path_cataua)
    st.image(img_cataua, caption='Queijo Catauá - Fazenda do Dutra', use_column_width=True)

    img_path_brumado = 'brumado_queijo.png'  
    img_brumado = Image.open(img_path_brumado)
    st.image(img_brumado, caption='Queijo do Brumado - Fazenda Brumado', use_column_width=True)

    img_path_cachacaria = 'cachacaria.png'  
    img_cachacaria = Image.open(img_path_cachacaria)
    st.image(img_cachacaria, use_column_width=True)

    img_path_seculo = 'seculo.png'  
    img_seculo = Image.open(img_path_seculo)
    st.image(img_seculo, caption='Cachaça Século XVIII - Engenho Boa Vista', use_column_width=True)

    img_path_c_jacuba = 'c_jacuba.png'  
    img_c_jacuba = Image.open(img_path_c_jacuba)
    st.image(img_c_jacuba, caption='Cachaça Jacuba- Hotel Fazenda Jacuba', use_column_width=True)

    img_path_demais = 'demais.png'  
    img_demais = Image.open(img_path_demais)
    st.image(img_demais, use_column_width=True)

    img_path_padaria = 'padaria.png'  
    img_padaria = Image.open(img_path_padaria)
    st.image(img_padaria, caption='Yaras padaria e pizzaria - Telefone de contato:(32) 99939-8884', use_column_width=True)

    img_path_lucas = 'lucas.png'  
    img_lucas = Image.open(img_path_lucas)
    st.image(img_lucas, caption='Casarão 35 - Telefone de contato:(32) 99914-9369', use_column_width=True)

    img_path_cocota = 'cocota.png'  
    img_cocota = Image.open(img_path_cocota)
    st.image(img_cocota, caption='Casaburger du Cocota - Telefone de contato: (32) 98459-5050', use_column_width=True)

    img_path_rogenia = 'rogenia_biscoito.png'  
    img_rogenia = Image.open(img_path_rogenia)
    st.image(img_rogenia, caption='Rogênia- Doces, biscoitos, iogurte, queijo, defumados - Telefone de contato: 32 99944-7243', use_column_width=True)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Botão Religiosidade 🙏

if paginaSelecionada == 'Religiosidade 🙏':
    img_path_religiosidade = 'Religiosidade.png'  
    img_religiosidade = Image.open(img_path_religiosidade)
    st.image(img_religiosidade, use_column_width=True)
    st.markdown(
        '''
        <p style="text-align: justify;">
        Aqui, a fé é um pilar fundamental na vida da comunidade! Celebramos eventos significativos como a Semana Santa e a Páscoa com reverência e devoção. A Festa de Nossa Senhora do Rosário é um momento de grande devoção, onde bandas de congadas enchem as ruas com música e devoção. E não podemos esquecer da grandiosa celebração da Festa da Padroeira, Nossa Senhora da Conceição, um momento especial de devoção e alegria para toda a cidade.
        </p>
        ''',
        unsafe_allow_html=True
    )
    img_path_rosario = 'rosario.png'  
    img_rosario = Image.open(img_path_rosario)
    st.image(img_rosario, caption='Festa em Honra a Nossa Senhora do Rosário', use_column_width=True)

    img_path_semana_santa = 'semana_santa.png'  
    img_semana_santa = Image.open(img_path_semana_santa)
    st.image(img_semana_santa, caption='Semana Santa', use_column_width=True)

    img_path_conceicao = 'conceicao.png'  
    img_conceicao = Image.open(img_path_conceicao)
    st.image(img_conceicao, caption='Festa em Honra a Padroeira Nossa Senhora da Conceição', use_column_width=True)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Botão Pontos Turísticos 🏞

if paginaSelecionada == 'Pontos Turísticos 🏞':
    img_path_turismo = 'Turismo.png'  
    img_turismo = Image.open(img_path_turismo)
    st.image(img_turismo, use_column_width=True)
    st.markdown(
        '''
        <p style="text-align: justify;">
        Prepare-se para se encantar com os lugares mais fascinantes de CXC! Visite o deslumbrante Mirante Bela Vista, onde a vista panorâmica vai te tirar o fôlego. Não deixe de conhecer a icônica Igreja Nossa Senhora do Rosário, carinhosamente chamada de 'Igrejinha de Pedra', um símbolo de fé e beleza arquitetônica. Explore as espetaculares fazendas, como a da Rogênia, que oferecem uma imersão na história e na beleza rural da região. E, é claro, todos os outros pontos já mencionados anteriormente, que fazem de CXC um destino imperdível para quem busca beleza e história.
        </p>
        ''',
        unsafe_allow_html=True
    )

    img_path_matriz = 'matriz.png'  
    img_matriz = Image.open(img_path_matriz)
    st.image(img_matriz, caption='Igreja Matriz de Nossa Senhora da Conceição', use_column_width=True)

    img_path_pedra = 'pedra.png'  
    img_pedra = Image.open(img_path_pedra)
    st.image(img_pedra, caption='Igreja de Nossa Senhora do Rosário, popularmente conhecido como Igrejinha de Pedra', use_column_width=True)

    img_path_mirante = 'mirante.png'  
    img_mirante = Image.open(img_path_mirante)
    st.image(img_mirante, caption='Mirante Bela Vista - "Santa"', use_column_width=True)

    img_path_rogenia_casa = 'rogenia_casa.png'  
    img_rogenia_casa = Image.open(img_path_rogenia_casa)
    st.image(img_rogenia_casa, caption='Casa da Rogênia- Comunidade do Sumidouro', use_column_width=True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
#Botão Festividades 🎉

if paginaSelecionada == 'Festividades 🎉':
    img_path_festividade = 'Festividades.png'  
    img_festividade = Image.open(img_path_festividade)
    st.image(img_festividade, use_column_width=True)
    st.markdown(
        '''
        <p style="text-align: justify;">
        As festas em Coronel são simplesmente imperdíveis! Desde o animado Carnaval até a agitada Exposição Agropecuária, passando pelo saboroso Festival do Queijo e Cachaça, e não podemos esquecer da adorada Moscoxaves - Cidade na Praça, um evento que une a comunidade e traz muita alegria. E quando o Natal se aproxima, a cidade se transforma em um verdadeiro conto de fadas, com ruas enfeitadas e shows encantadores que preparam todos para a festa de final de ano. São celebrações que enchem Coronel de vida e energia durante o ano todo!
        </p>
        ''',
        unsafe_allow_html=True
    )
    img_path_carnaval = 'carnaval.png'  
    img_carnaval = Image.open(img_path_carnaval)
    st.image(img_carnaval, caption='Carnaval', use_column_width=True)

    img_path_queijo_cachaca = 'queijo_cachaca.png'  
    img_queijo_cachaca = Image.open(img_path_queijo_cachaca)
    st.image(img_queijo_cachaca, caption='Festival do Queijo e Cachaça de Coronel Xavier Chaves', use_column_width=True)

    img_path_mosco = 'mosco.png'  
    img_mosco = Image.open(img_path_mosco)
    st.image(img_mosco, caption='Moscoxaves- Mostra Cultural de Desenvolvimento Econômico de Coronel Xavier Chaves', use_column_width=True)

    img_path_natal = 'natal.png'  
    img_natal = Image.open(img_path_natal)
    st.image(img_natal, caption='Natal Encantado', use_column_width=True)

    img_path_expo = 'expo.png'  
    img_expo = Image.open(img_path_expo)
    st.image(img_expo, caption='Exposição Agropecuária', use_column_width=True)





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Botão Rotas🗺

if paginaSelecionada == 'Rotas🗺':
    img_path_rotas = 'Rotas.png'  
    img_rotas = Image.open(img_path_rotas)
    st.image(img_rotas, use_column_width=True)
    st.markdown(
        '''
        <p style="text-align: justify;">
        Coronel Xavier Chaves, município encantador situado no estado de Minas Gerais, é um verdadeiro tesouro em termos de rotas pitorescas e fascinantes. Suas estradas sinuosas levam os viajantes a descobrirem paisagens deslumbrantes e experiências memoráveis.

        <a href="https://www.google.com.br/maps/place/Jequitib%C3%A1+Hist%C3%B3rico/@-21.0042165,-44.2425074,1073m/data=!3m2!1e3!4b1!4m6!3m5!1s0xa1bb26783146f7:0x2fa50caf4a23a663!8m2!3d-21.0042165!4d-44.2425074!16s%2Fg%2F11mttwm3z5!5m1!1e4?entry=ttu">Árvore de Jequitibá</a><br>
        <a href="https://www.google.com.br/maps/dir/Igreja+de+Pedra+(Nossa+Senhora+do+Ros%C3%A1rio)+-+Rua+Monsenhor+Parreira,+Coronel+Xavier+Chaves+-+MG/Cachoeira+Bau,+Cel.+Xavier+Chaves+-+MG,+36330-000/@-21.0050035,-44.2322393,4290m/data=!3m2!1e3!4b1!4m14!4m13!1m5!1m1!1s0xa1ba26d79be88f:0xb4738646a6d5c22a!2m2!1d-44.2236582!2d-21.0215118!1m5!1m1!1s0xa1ba5e5a2a1445:0x67fc807a4e0784d9!2m2!1d-44.226874!2d-20.988388!3e0!5m1!1e4?entry=ttu">Cachoeira do Baú</a><br>
        <a href="https://www.google.com.br/maps/dir/Igreja+de+Pedra+(Nossa+Senhora+do+Ros%C3%A1rio)+-+Rua+Monsenhor+Parreira,+Coronel+Xavier+Chaves+-+MG/Mirante+N+Sra,+Cel.+Xavier+Chaves+-+MG,+36330-000/@-21.0191747,-44.2292513,1072m/data=!3m2!1e3!4b1!4m14!4m13!1m5!1m1!1s0xa1ba26d79be88f:0xb4738646a6d5c22a!2m2!1d-44.2236582!2d-21.0215118!1m5!1m1!1s0xa1ba1f63163809:0xc2371cc8594bd0cb!2m2!1d-44.229141!2d-21.0191779!3e2!5m1!1e4?entry=ttu">Mirante Bela Vista</a><br>
        <a href="https://www.google.com.br/maps/dir/Igreja+de+Pedra+(Nossa+Senhora+do+Ros%C3%A1rio)+-+Rua+Monsenhor+Parreira,+Coronel+Xavier+Chaves+-+MG/Cacha%C3%A7a+Jacuba+-+Rodovia+Vereador+Jo%C3%A3o+Vicente+Vieira+Camargo.+-+Zona+Rural,+Cel.+Xavier+Chaves+-+MG,+36330-000/@-21.0354907,-44.2229249,4289m/data=!3m2!1e3!4b1!4m14!4m13!1m5!1m1!1s0xa1ba26d79be88f:0xb4738646a6d5c22a!2m2!1d-44.2236582!2d-21.0215118!1m5!1m1!1s0xa1b972d90b0fdf:0xf99268b33fa167c6!2m2!1d-44.2002536!2d-21.0468086!3e2!5m1!1e4?entry=ttu">Cachaça Jacuba</a><br>
        <a href="hhttps://www.google.com.br/maps/dir/Igreja+de+Pedra+(Nossa+Senhora+do+Ros%C3%A1rio)+-+Rua+Monsenhor+Parreira,+Coronel+Xavier+Chaves+-+MG/Cacha%C3%A7aria+Seculo+XVIII+-+R.+Jo%C3%A3o+XXIII,+443,+Cel.+Xavier+Chaves+-+MG,+36330-000/@-21.023437,-44.227784,536m/data=!3m2!1e3!4b1!4m14!4m13!1m5!1m1!1s0xa1ba26d79be88f:0xb4738646a6d5c22a!2m2!1d-44.2236582!2d-21.0215118!1m5!1m1!1s0xa1b98b1fa932df:0x504023d7262fefd2!2m2!1d-44.229334!2d-21.0255751!3e2!5m1!1e4?entry=ttu">Cachaça Século XVIII</a><br>
        <a href="https://www.google.com.br/maps/dir/Igreja+de+Pedra+(Nossa+Senhora+do+Ros%C3%A1rio)+-+Rua+Monsenhor+Parreira,+Coronel+Xavier+Chaves+-+MG/Sumidouro+-+Unnamed+Road,+Cel.+Xavier+Chaves+-+MG,+36330-000/@-20.9989789,-44.2292905,8580m/data=!3m2!1e3!4b1!4m14!4m13!1m5!1m1!1s0xa1ba26d79be88f:0xb4738646a6d5c22a!2m2!1d-44.2236582!2d-21.0215118!1m5!1m1!1s0xa1bb7b02e78d93:0x877e047b2211532c!2m2!1d-44.193218!2d-20.9866243!3e2!5m1!1e4?entry=ttu">Fazenda da Rogênia</a><br>
        </p>
        Essas são apenas algumas das principais rotas que Coronel Xavier Chaves oferece aos exploradores e aventureiros. Cada uma delas proporciona uma experiência única, seja pela beleza natural, riqueza histórica ou pelo contato genuíno com a cultura local. Viajar por esses caminhos é descobrir um pouco mais sobre a riqueza e diversidade que esse município mineiro tem a oferecer.
        ''',
        unsafe_allow_html=True
    )


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Botão Clima☀

if paginaSelecionada == 'Clima☀️':
    img_path_clima = 'Clima.png'  
    img_clima = Image.open(img_path_clima)
    st.image(img_clima, use_column_width=True)
    st.markdown(
        '''
        Coronel Xavier Chaves, localizado no estado de Minas Gerais, apresenta um clima tropical de altitude. Caracteriza-se por estações bem definidas ao longo do ano, com verões quentes e úmidos e invernos mais amenos e secos.
        <p style="text-align: justify;">
        <a href="https://www.climatempo.com.br/previsao-do-tempo/cidade/3685/coronelxavierchaves-mg">Clima da Cidade de Coronel Xavier Chaves</a><br>
        </p>
        Essa diversidade climática de Coronel Xavier Chaves proporciona uma experiência agradável aos visitantes, permitindo que desfrutem das diferentes nuances das estações e explorem as belezas naturais em cada período do ano.
        ''',
        unsafe_allow_html=True
    )
 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
# Botão Patrocinadores💸

if paginaSelecionada == 'Patrocinadores💸':
    img_path_patrocinadores = 'Patrocinadores.png'  
    img_patrocinadores = Image.open(img_path_patrocinadores)
    st.image(img_patrocinadores, use_column_width=True)
    
    st.markdown('<p style="text-align: justify;">Patrocinadores:</p>', unsafe_allow_html=True)
    
    patrocinadores = [
        'Lili Longati Bainhas e  Bordados',
        'Depósito Xavierense',
        'Oficina Pau Brasil',
        'Rogênia',
        'Mimos Laços e Luxos',
        'Marcia Roberta Atelier',
        'Auto Escola Lara',
        'Rogério Móveis'
    ]

    for patrocinador in patrocinadores:
        st.write(f"- {patrocinador}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Botão "Quem sou eu?😊"

if paginaSelecionada == "Sobre😊":
    img_path_eu = 'eu.png'  
    img_eu = Image.open(img_path_eu)
    st.image(img_eu, use_column_width=True)
    
    img_path_marcela = 'marcela.png'  
    img_marcela = Image.open(img_path_marcela)
    st.image(img_marcela, use_column_width=True)

    st.markdown(
        '''
        <p style="text-align: justify;">
        Sou a Marcela Longati Pinto, tenho 21 anos e atuo como analista técnica de suporte na SH3. Atualmente, estou me dedicando aos estudos de Gestão Pública. Recentemente, mergulhei no universo do Python e descobri o quão versátil e funcional essa linguagem de programação pode ser. Acredito que esse conhecimento será extremamente útil em minha jornada profissional.

        Gostaria de expressar minha gratidão ao professor que me guiou nesse aprendizado, à equipe do Senai pela oportunidade e a todos os colegas de curso, cuja colaboração foi fundamental para o meu crescimento nesse campo tão interessante e desafiador.

        Além disso, não posso deixar de expressar minha gratidão à Prefeitura Municipal pelo comprometimento e pela oportunidade de fazer parte desse processo. A colaboração e apoio oferecidos foram essenciais para o meu crescimento profissional e pessoal. Agradeço sinceramente pela confiança e pela chance de contribuir para a comunidade através dessa experiência enriquecedora.
        </p>
        <a href="https://coronelxavierchaves.mg.gov.br/prefeitura/">Demais informações</a><br>

        ''',
        unsafe_allow_html=True
        )
    img_path_obrigada = 'obrigada.png'  
    img_obrigada = Image.open(img_path_obrigada)
    st.image(img_obrigada, use_column_width=True)

