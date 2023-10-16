



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 4")
st.sidebar.markdown("# Quiz du chapitre 4")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/analyze_this.gif')

st.title("Segmentation et analyse de l'offre de main-d'œuvre")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours de **Segmentation et analyse de l'offre de main-d'œuvre**.")

st.markdown("Cocher les bonnes réponses.")

st.subheader("1/ Dans le contexte de la planification stratégique de la main-d'œuvre, quel est l'objectif principal de la catégorisation de la main-d'œuvre en fonction de ses rôles critiques ?")

check = st.checkbox("a) Déterminer les rôles les plus populaires dans l'organisation", key="check1")
if check:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_2 = st.checkbox("b) S'assurer que les salariés d'une même catégorie possèdent des compétences identiques", key="check2")
if check_2:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_3 = st.checkbox("c) Créer une atmosphère de compétition entre les employés", key="check3")
if check_3:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_4 = st.checkbox("d) Concentrer les ressources et les efforts sur les rôles qui influencent de manière significative les objectifs stratégiques", key="check4")
if check_4:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
    

st.subheader("2/ En quoi consiste l’analyse de l’offre de main d’œuvre ?")

check_5 = st.checkbox("a) Évaluation de la disponibilité des fournitures de bureau pour les employés", key="check5")
if check_5:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_6 = st.checkbox("b) Évaluer les sources de talents internes et externes pour répondre aux besoins de l'organisation", key="check6")
if check_6:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
check_7 = st.checkbox("c) Évaluation des aptitudes et des compétences des candidats externes", key="check7")
if check_7:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_8 = st.checkbox("d) Réaliser une analyse financière de la chaîne d'approvisionnement de l'organisation", key="check8")
if check_8:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################


st.subheader("3/ Pourquoi la planification de la succession et la constitution d’un vivier de talents sont-elles essentielles ?")

check_9 = st.checkbox("a) Pour s'assurer que tous les employés reçoivent des promotions sur une base régulière")

if check_9:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_10 = st.checkbox("b) Pour créer une structure organisationnelle hiérarchique")

if check_10:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_11 = st.checkbox("c) Pour préparer les talents internes à remplir des rôles critiques à l'avenir ")

if check_11:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_12 = st.checkbox("d) Pour minimiser le besoin de recrutement et d'embauches externes")

if check_12:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.markdown("")


def redirect_button(url: str, text: str= None, color="#FD504D"):
        st.markdown(
        f"""
        <a href="{url}" target="_blank">
            <div style="
                display: inline-block;
                padding: 0.5em 1em;
                color: #FFFFFF;
                background-color: {color};
                border-radius: 3px;
                text-decoration: none;">
                {text}
            </div
        </a>
        """,
        unsafe_allow_html=True
        )
redirect_button("https://gpec-gepp.streamlit.app/Chapitre_5_🔖_Élaborer_le_plan_stratégique_de_main-d’œuvre","Aller au chapitre 5")




