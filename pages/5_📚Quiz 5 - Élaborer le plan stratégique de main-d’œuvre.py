



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 5")
st.sidebar.markdown("# Quiz du chapitre 5")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/analyze_this.gif')

st.title("Élaborer le plan stratégique de main-d’œuvre")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours d'**Élaboration du plan stratégique de main-d’œuvre**.")

st.markdown("Cocher les bonnes réponses.")

st.subheader("1/ Quelle est la première étape dans l’élaboration d’un plan stratégique de main-d’œuvre ?")

check = st.checkbox("a) Créer un plan d'action pour l'acquisition de talents", key="check1")
if check:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_2 = st.checkbox("b) Évaluation de la main-d'œuvre actuelle", key="check2")
if check_2:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_3 = st.checkbox("c) Réaliser une analyse des déficits de compétences", key="check3")
if check_3:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_4 = st.checkbox("d) Définir les objectifs et buts stratégiques", key="check4")
if check_4:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
    

st.subheader("2/ Quel est l’objectif principal de la création de plans d’action ?")

check_5 = st.checkbox("a) Décrire les activités de consolidation d'équipe", key="check5")
if check_5:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_6 = st.checkbox("b) Combler les pénuries de talents et combler les pénuries de compétences", key="check6")
if check_6:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
check_7 = st.checkbox("c) Établir un calendrier d'évaluations annuelles des performances", key="check7")
if check_7:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_8 = st.checkbox("d) Planifier des pique-niques à l'échelle de l'entreprise", key="check8")
if check_8:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################


st.subheader("3/ Pourquoi l’élaboration d’une stratégie d’acquisition et de rétention des talents est-elle une partie importante du processus de planification stratégique ?")

check_9 = st.checkbox("a) Pour augmenter le turnover et réduire l’ancienneté des employés")

if check_9:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_10 = st.checkbox("b) Pour garantir que les employés disposent de possibilités limitées d’évolution de carrière")

if check_10:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_11 = st.checkbox("c) Pour créer une feuille de route pour attirer et retenir les meilleurs talents alignés sur les objectifs stratégiques de l'organisation")

if check_11:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_12 = st.checkbox("d) Pour minimiser les investissements dans les programmes de formation et de développement")

if check_12:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################



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
redirect_button("https://gpec-gepp.streamlit.app/Chapitre_6_🔖_Mise_en_œuvre_et_gestion_du_changement","Aller au chapitre 6")




