



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 6")
st.sidebar.markdown("# Quiz du chapitre 6")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/bPDKEmlJ.gif')

st.title("Mise en œuvre et gestion du changement")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours de **Mise en œuvre et gestion du changement**.")

st.markdown("Cocher les bonnes réponses.")

st.subheader("1/ Quel est l’objectif principal du déploiement d’un plan de main-d’œuvre pendant la phase d'implémentation ?")

check = st.checkbox("a) Apporter des changements immédiats à l'effectif de l'organisation", key="check1")
if check:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_2 = st.checkbox("b) Fournir un plan détaillé des vacances des employés", key="check2")
if check_2:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_3 = st.checkbox("c) Éliminer le besoin d'une gestion continue des ressources humaines", key="check3")
if check_3:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_4 = st.checkbox("d) Mettre efficacement la planification stratégique en action, en garantissant son alignement sur les objectifs stratégiques", key="check4")
if check_4:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
    

st.subheader("2/ Pourquoi une communication efficace avec les parties prenantes est-elle cruciale lors de la mise en œuvre de la planification stratégique des effectifs ?")

check_5 = st.checkbox("a) Pour minimiser la communication et garder les parties prenantes dans l'ignorance des changements", key="check5")
if check_5:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_6 = st.checkbox("b) Pour favoriser la compréhension, obtenir l’adhésion et garantir que toutes les parties sont informées et engagées", key="check6")
if check_6:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
check_7 = st.checkbox("c) Pour maintenir le secret et éviter d’impliquer les parties prenantes dans le processus", key="check7")
if check_7:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_8 = st.checkbox("d) Pour promouvoir les conflits et les désaccords entre les parties prenantes", key="check8")
if check_8:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################


st.subheader("3/ Quel est l’objectif principal de la gestion du changement organisationnel pendant la mise en œuvre de la planification stratégique des effectifs ?")

check_9 = st.checkbox("a) éviter tout changement et maintenir le statu quo")

if check_9:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_10 = st.checkbox("b) Apporter des changements brusques et perturbateurs à l'organisation")

if check_10:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_11 = st.checkbox("c) Aider les employés à traverser en douceur les changements et à s'adapter au nouveau plan de main-d'œuvre")

if check_11:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_12 = st.checkbox("d) Créer de la confusion et du chaos au sein de l'organisation")

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
redirect_button("https://gpec-gepp.streamlit.app/Chapitre_7_🔖_Contrôle_et_évaluation","Aller au chapitre 7")




