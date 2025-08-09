from pathlib import Path
import streamlit as st
from PIL import Image

#configuraçoes estruturais
diretorio = Path(__file__).parent if '__file__' in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "geral.css"
arquivo_pdf = diretorio / "assets" / "curriculo_andre.pdf"
arquivo_img = diretorio / "assets" / "foto.jpg"

#configuraçoes gerais de informaçoes    

TITULO = "Currículo | André Barbosa"
NOME = "André Barbosa"
DESCRICAO = """
    Em busca de oportunidades para entrar de vez no mundo do desenvolvimento web, Dev front end, back end e Full Stack. Curto criar, aprender e me desafiar, sempre com vontade de evoluir rápido e fazer parte de projetos que gerem impacto de verdade.
"""
EMAIL = "andbar3211@hotmail.com"
MIDIA_SOCIAL = {
    "GitHub": "https://github.com/AndreBarbosa-03",
    "LinkedIn": "https://www.linkedin.com/in/andrevibarbosa/"
}

#configuraçoes de layout

st.set_page_config(
    page_title= TITULO
)

#carregando assets  

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)
with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
image = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(image, width=250)
with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label="Baixar currículo",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
    )
    st.write("📫", EMAIL)

#midias sociais
st.write("#")
columns = st.columns(len(MIDIA_SOCIAL))
for indice, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    columns[indice].write(f"[{plataforma}]({link})")

#formação
st.write("#")
st.subheader("Formação Acadêmica")
st.write("""
    - 🎓 Graduando em Analise e Desenvolvimento de Sistemas - Faculdade Anhanguera - Belo Horizonte 
""")

#experiencias
st.write("#")
st.subheader("Experiências")   
st.write(
    """
    - 📊 Utilizei tecnologia e automação para transformar o controle de suprimentos em processos mais ágeis e integrados, garantindo precisão e velocidade na gestão via SAP.
    - 📈 Converti dados e rotinas administrativas em informações estratégicas, criando planilhas e fluxos inteligentes que impulsionaram o controle financeiro e operacional.
    - 🗂️ Apliquei organização e análise de dados para otimizar relatórios e documentos, facilitando a tomada de decisão e melhorando o fluxo administrativo.
"""
)

#skills
st.write("#")
st.subheader("Skills")
st.write(
    """
    - ⚖️ Análise de Risco e Tomada de Decisão. 
    - ⚡ Metodologias Ágeis.
    - 🗄️ Estrutura e Arquitetura de Dados.
    - 🐍 Python.
    - 🎤 Comunicação e Apresentação de Alto Impacto.
    """
)   
#historico profissional
st.write("#")
st.subheader("Histórico Profissional")
st.write("---")   

#1 contrato
st.write("🗂️""**Aprendiz Administrativo | Rede Cidadã**")
st.write("06/2018 – 05/2019")
st.write(
    """
    Na Rede Cidadã, apliquei organização e análise de dados para otimizar relatórios e documentos, facilitando a tomada de decisão e melhorando o fluxo administrativo.
"""
)

#2 contrato
st.write("📈""**Auxiliar Administrativo II | Vaccinar**")
st.write("05/2019 – 03/2023")
st.write(
    """
    Na Vaccinar, converti dados e rotinas administrativas em informações estratégicas, criando planilhas e fluxos inteligentes que impulsionaram o controle financeiro e operacional.
"""
)

#3 contrato
st.write("📊""**Assistente de Suprimentos GPD | MRV&CO**")
st.write("08/2023 – 12/2024")
st.write(
    """
    Na MRV&CO, utilizei tecnologia e automação para transformar o controle de suprimentos em processos mais ágeis e integrados, garantindo precisão e velocidade na gestão via SAP.
"""
)