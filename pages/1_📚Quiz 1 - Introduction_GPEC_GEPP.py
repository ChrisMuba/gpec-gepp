



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 1")
st.sidebar.markdown("# Quiz du chapitre 1")

# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/copiste.gif')

st.title("Introduction à la planification stratégique des effectifs")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours d'introduction à la GPEC, GEPP et à la planification stratégique.")

st.markdown("Cocher les bonnes réponses.")

st.subheader("1/ Quel est l’objectif principal de la planification stratégique des effectifs ?")

check = st.checkbox("a) Gérer les tâches RH quotidiennes")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Aligner les effectifs sur les objectifs stratégiques")

if check_2:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_3 = st.checkbox("c) Améliorer l'engagement des employés")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Réduire les coûts opérationnels")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.subheader("2/  Comment le rôle des RH a-t-il évolué ces dernières années ?")

check = st.checkbox("a) L'attention des RH s'est déplacée uniquement vers les tâches administratives.")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b)  Les RH sont devenues moins impliquées dans la planification stratégique.")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Les responsabilités RH excluent désormais le développement des talents.")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Les RH se sont transformées en partenaire stratégique des organisations.")

if check_4:
   st.write("👏🏾**Bonne réponse !** 👍🏾")


st.subheader("3/ Pourquoi est-il crucial de lier la planification des effectifs à la stratégie commerciale ?")

check = st.checkbox("a) Cela simplifie les responsabilités des RH.")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Pour garantir le respect des normes de l’industrie")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Cela permet à l'organisation de relever de manière proactive les défis liés à la main-d'œuvre.")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Cela réduit le besoin d’évaluations de performance")

if check_4:
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
redirect_button("https://gpec-gepp.streamlit.app/Chapitre_2_🔖_Analyse_de_la_main-d'œuvre_et_collecte_de_données","Aller au chapitre 2")




