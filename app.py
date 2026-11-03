import streamlit as st

# DADOS COMPLETOS (Integridade Total Preservada - v35.1)
DADOS_AVES = {
    "Tentilhão": {"familia": "Fringillidae", "genero": "Fringilla", "tamanho": 15},
    "Tentilhão-montês": {"familia": "Fringillidae", "genero": "Fringilla", "tamanho": 15},
    "Tentilhão-azul": {"familia": "Fringillidae", "genero": "Fringilla", "tamanho": 16},
    "Canário-doméstico": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 14},
    "Canário-bravo": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Chamariz": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 11},
    "Verdilhão-serrano": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Saramugo": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Milheirinha": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Milheirinha-da-córsega": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Chamariz-de-testa-vermelha": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 11},
    "Pintassilgo": {"familia": "Fringillidae", "genero": "Carduelis", "tamanho": 12},
    "Verdilhão": {"familia": "Fringillidae", "genero": "Chloris", "tamanho": 15},
    "Lugre": {"familia": "Fringillidae", "genero": "Spinus", "tamanho": 11},
    "Pintarroxo": {"familia": "Fringillidae", "genero": "Linaria", "tamanho": 13},
    "Pintarroxo-de-bico-amarelo": {"familia": "Fringillidae", "genero": "Linaria", "tamanho": 13},
    "Pintarroxo-áxico": {"familia": "Fringillidae", "genero": "Acanthis", "tamanho": 13},
    "Pintarroxo-de-cabeça-vermelha": {"familia": "Fringillidae", "genero": "Acanthis", "tamanho": 13},
    "Pintarroxo-ártico": {"familia": "Fringillidae", "genero": "Acanthis", "tamanho": 14},
    "Dom-fafe": {"familia": "Fringillidae", "genero": "Pyrrhula", "tamanho": 16},
    "Dom-fafe-dos-açores": {"familia": "Fringillidae", "genero": "Pyrrhula", "tamanho": 15},
    "Bico-grossudo": {"familia": "Fringillidae", "genero": "Coccothraustes", "tamanho": 18},
    "Cruza-bico-comum": {"familia": "Fringillidae", "genero": "Loxia", "tamanho": 17},
    "Cruza-bico-das-pinhas": {"familia": "Fringillidae", "genero": "Loxia", "tamanho": 18},
    "Cruza-bico-escocês": {"familia": "Fringillidae", "genero": "Loxia", "tamanho": 17},
    "Cruza-bico-de-duas-faixas": {"familia": "Fringillidae", "genero": "Loxia", "tamanho": 16},
    "Pintarroxo-de-peito-rosa": {"familia": "Fringillidae", "genero": "Carpodacus", "tamanho": 15},
    "Trompeteiro": {"familia": "Fringillidae", "genero": "Bucanetes", "tamanho": 15},
    "Pinheirão": {"familia": "Fringillidae", "genero": "Pinicola", "tamanho": 22},
    "Pintarroxo-de-bico-grosso": {"familia": "Fringillidae", "genero": "Eophona", "tamanho": 19},
    "Canário-de-cabeça-preta": {"familia": "Fringillidae", "genero": "Spinus", "tamanho": 11},
    "Lugre-de-peito-preto": {"familia": "Fringillidae", "genero": "Spinus", "tamanho": 11},
    "Pintassilgo-de-cabeça-preta": {"familia": "Fringillidae", "genero": "Carduelis", "tamanho": 13},
    "Pintassilgo-oriental": {"familia": "Fringillidae", "genero": "Carduelis", "tamanho": 13},
    "Pintassilgo-do-himalaia": {"familia": "Fringillidae", "genero": "Carduelis", "tamanho": 14},
    "Verdilhão-do-himalaia": {"familia": "Fringillidae", "genero": "Chloris", "tamanho": 14},
    "Verdilhão-chinês": {"familia": "Fringillidae", "genero": "Chloris", "tamanho": 14},
    "Verdilhão-de-peito-amarelo": {"familia": "Fringillidae", "genero": "Chloris", "tamanho": 14},
    "Chamariz-de-bico-grosso": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 13},
    "Chamariz-de-barriga-branca": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Chamariz-da-síria": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Chamariz-de-moçambique": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Dom-fafe-de-cabeça-cinza": {"familia": "Fringillidae", "genero": "Pyrrhula", "tamanho": 15},
    "Dom-fafe-de-peito-vermelho": {"familia": "Fringillidae", "genero": "Pyrrhula", "tamanho": 16},
    "Trompeteiro-mongol": {"familia": "Fringillidae", "genero": "Bucanetes", "tamanho": 14},
    "Pintarroxo-de-bico-grosso-asiático": {"familia": "Fringillidae", "genero": "Eophona", "tamanho": 20},
    "Pintarroxo-de-peito-rosa-asiático": {"familia": "Fringillidae", "genero": "Carpodacus", "tamanho": 15},
    "Carpodaco-de-cabeça-vermelha": {"familia": "Fringillidae", "genero": "Carpodacus", "tamanho": 15},
    "Carpodaco-de-sobrancelha-branca": {"familia": "Fringillidae", "genero": "Carpodacus", "tamanho": 16},
    "Pintarroxo-de-asas-brancas": {"familia": "Fringillidae", "genero": "Loxia", "tamanho": 16},
    "Cruza-bico-de-himalaia": {"familia": "Fringillidae", "genero": "Loxia", "tamanho": 17},
    "Serinus-alario": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Serinus-canicollis": {"familia": "Fringillidae", "genero": "Serinus", "tamanho": 12},
    "Cardealito da Venezuela": {"familia": "Fringillidae", "genero": "Carduelis", "tamanho": 10},
}

PROTOCOLOS_BASE_ESPECIE = {ave: {"Dif": "Média", "Foto": "14h", "Dieta": "Mistura base + sementes germinadas.", "Época": "Mar-Jul", "Manejo": "Higiene regular e proteção."} for ave in DADOS_AVES}
PROTOCOLOS_BASE_ESPECIE["Canário-doméstico"] = {"Dif": "Baixa", "Foto": "15h", "Dieta": "Mistura alpista/nabão + papa.", "Época": "Mar-Jun", "Manejo": "Banho diário essencial."}
PROTOCOLOS_BASE_ESPECIE["Pintassilgo"] = {"Dif": "Alta", "Foto": "15h", "Dieta": "Mistura silvestres + cardo.", "Época": "Abr-Jul", "Manejo": "Ninho camuflado vital."}

PROTOCOLOS_HIBRIDACAO = {
    ("Pintassilgo", "Canário-doméstico"): {"Prob": 85, "Fert": "F1 Machos: Férteis; F1 Fêmeas: Estéreis.", "Viab": "Elevada.", "Manejo": "Uso de amas canárias e grade separadora."},
    ("Verdilhão", "Canário-doméstico"): {"Prob": 70, "Fert": "F1 Machos: Férteis; F1 Fêmeas: Frequente esterilidade.", "Viab": "Boa; robustos.", "Manejo": "Viveiro amplo necessário."}
}

def obter_protocolo_especialista(m, f):
    if m == f:
        return {"Prob": 100, "Fert": "100% Fértil (Acasalamento Intraespecífico).", "Viab": "Máxima", "Manejo": "Manter protocolos padrão."}
    if (m, f) in PROTOCOLOS_HIBRIDACAO: return PROTOCOLOS_HIBRIDACAO[(m, f)]
    if (f, m) in PROTOCOLOS_HIBRIDACAO: return PROTOCOLOS_HIBRIDACAO[(f, m)]
    
    m_data, f_data = DADOS_AVES[m], DADOS_AVES[f]
    if m_data['genero'] == f_data['genero']:
        return {"Prob": 75, "Fert": "F1 Machos: Férteis; F1 Fêmeas: Potencial esterilidade (Regra de Haldane).", "Viab": "Elevada", "Manejo": "Monitorizar acasalamento; ninho misto."}
    elif m_data['familia'] == f_data['familia']:
        return {"Prob": 35, "Fert": "F1 Machos: Fertilidade variável; F1 Fêmeas: Estéreis.", "Viab": "Moderada", "Manejo": "Uso de amas e separação de segurança."}
    return {"Prob": 5, "Fert": "Improvável.", "Viab": "Muito baixa.", "Manejo": "Não recomendado."}

# Interface Streamlit
st.set_page_config(page_title="OrnithoExpert", page_icon="🐦")
st.title("🐦 OrnithoExpert Web")

col1, col2 = st.columns(2)
with col1: macho = st.selectbox("Escolha o Macho:", sorted(DADOS_AVES.keys()))
with col2: femea = st.selectbox("Escolha a Fêmea:", sorted(DADOS_AVES.keys()))

if st.button("Gerar Parecer Técnico"):
    h = obter_protocolo_especialista(macho, femea)
    
    st.subheader("--- Parecer Técnico ---")
    st.success(f"Probabilidade estimada: {h['Prob']}%")
    st.write(f"**Fertilidade:** {h['Fert']}")
    st.write(f"**Viabilidade:** {h['Viab']}")
    st.write(f"**Manejo Especialista:** {h['Manejo']}")
    
    st.subheader("--- Protocolos de Manejo Individual ---")
    for ave in [macho, femea]:
        p = PROTOCOLOS_BASE_ESPECIE.get(ave)
        with st.expander(f"Protocolo: {ave}"):
            st.write(f"**Dificuldade:** {p['Dif']} | **Fotoperíodo:** {p['Foto']}")
            st.write(f"**Dieta:** {p['Dieta']}")
            st.write(f"**Época:** {p['Época']}")
            st.write(f"**Manejo:** {p['Manejo']}")
