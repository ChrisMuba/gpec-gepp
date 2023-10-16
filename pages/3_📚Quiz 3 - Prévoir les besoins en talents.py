



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 3")
st.sidebar.markdown("# Quiz du chapitre 2")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/analyze_this.gif')

st.title("Prévision des besoins en talents")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours de **Prévision des besoins en talents**.")

st.markdown("Cocher les bonnes réponses.")

st.subheader("1/ Parmi les méthodes suivantes, laquelle est couramment utilisée pour prédire les besoins futurs en main-d'œuvre dans la planification stratégique des effectifs ?")

check = st.checkbox("a) Analyse des conditions météorologiques historiques", key="check1")
if check:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_2 = st.checkbox("b) Évaluation des scores de satisfaction client", key="check2")
if check_2:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_3 = st.checkbox("c) Évaluation des niveaux d'engagement actuels des employés", key="check3")
if check_3:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_4 = st.checkbox("d) Examen des tendances du secteur et des projections de croissance", key="check4")
if check_4:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
    

st.subheader("2/ Quel est l’objectif principal de la planification de scénarios et de la modélisation des effectifs dans la prévision des talents ?")

check_5 = st.checkbox("a) Pour prédire les numéros de loterie des employés", key="check5")
if check_5:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_6 = st.checkbox("b) Explorer différents scénarios et leur impact potentiel sur les besoins en main-d'œuvre", key="check6")
if check_6:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
check_7 = st.checkbox("c) Déterminer les meilleurs emplacements pour le travail à distance", key="check7")
if check_7:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_8 = st.checkbox("d) Pour calculer le coût des programmes de formation des employés", key="check8")
if check_8:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################


st.subheader("1/ Pourquoi l’identification des rôles et compétences critiques est-elle essentielle dans la prévision des talents ?")

check_9 = st.checkbox("a) Garantir à tous les employés des chances égales de promotion")

if check_9:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_10 = st.checkbox("b) Déterminer quels employés sont les plus populaires au sein de l'organisation")

if check_10:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_11 = st.checkbox("c) Aligner les efforts de développement des talents sur les objectifs stratégiques")

if check_11:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_12 = st.checkbox("d) Pour comprendre quels rôles ont les salaires les plus élevés")

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
redirect_button("https://gpec-gepp.streamlit.app/Chapitre_4_🔖_Segmentation_et_analyse_de_l’offre_de_main-d’œuvre","Aller au chapitre 4")




