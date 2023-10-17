



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 7")
st.sidebar.markdown("# Quiz du chapitre 7")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/analyze_this.gif')

st.title("Suivi et Évaluation")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours de **Suivi et Évaluation**.")

st.markdown("Cocher les bonnes réponses.")

st.subheader("1/ Pourquoi les KPI et autres métriques sont-ils cruciaux dans le suivi et l'évaluation d'un plan stratégique de main-d'œuvre ?")

check = st.checkbox("a) Pour fournir un moyen de classer les employés en fonction de leurs performances.", key="check1")
if check:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_2 = st.checkbox("b) Pour servir de référence pour comparer les performances des RH avec celles des autres services.", key="check2")
if check_2:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_3 = st.checkbox("c) Pour se concentrer uniquement sur la performance financière et les marges bénéficiaires.", key="check3")
if check_3:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_4 = st.checkbox("d) Pour aider à mesurer l’alignement de la main-d’œuvre sur les objectifs stratégiques et à suivre les progrès.", key="check4")
if check_4:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
    

st.subheader("2/ À quelle fréquence les évaluations périodiques des effectifs doivent-elles généralement avoir lieu pendant la mise en œuvre de la planification stratégique ?")

check_5 = st.checkbox("a) Mensuellement", key="check5")
if check_5:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_6 = st.checkbox("b) Cela dépend des besoins spécifiques de l'organisation", key="check6")
if check_6:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
check_7 = st.checkbox("c) Annuellement", key="check7")
if check_7:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_8 = st.checkbox("d) Aussi rarement que possible", key="check8")
if check_8:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################


st.subheader("3/ Quel est l’objectif principal de l’évaluation de l’efficacité d’un plan stratégique de main-d’œuvre ?")

check_9 = st.checkbox("a) Évaluer l'impact du plan sur l'efficacité du service RH")

if check_9:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_10 = st.checkbox("b) Pour vérifier si le plan correspond au logo et à l'image de marque de l'organisation")

if check_10:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_11 = st.checkbox("c) Mesurer la contribution du plan à la réalisation des objectifs stratégiques et apporter les ajustements nécessaires")

if check_11:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_12 = st.checkbox("d) Classer les employés en fonction de leurs performances")

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
redirect_button("https://gpec-gepp.streamlit.app/Chapitre_7_🔖_Suivi_et_évaluation","Aller au chapitre 3")




