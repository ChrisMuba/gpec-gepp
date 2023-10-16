



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 2")
st.sidebar.markdown("# Quiz du chapitre 2")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/analyze_this.gif')

st.title("Analyse de la main-d'œuvre et collecte de données")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours d'**analyse de la main-d'œuvre et la collecte de données**.")

st.markdown("Cocher les bonnes réponses.")

st.subheader("1/ Quel est l’objectif principal de la réalisation d’une analyse des déficits de compétences dans la planification de la main-d’œuvre ?")

check = st.checkbox("a) Identifier les programmes de formation les plus rentables", key="check1")
if check:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_2 = st.checkbox("b) Comparer la performance financière de l'entreprise avec les normes de l'industrie", key="check2")
if check_2:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_3 = st.checkbox("c) Évaluer les stratégies marketing de l'organisation", key="check3")
if check_3:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_4 = st.checkbox("d) Évaluer la disparité entre les compétences requises et les compétences actuelles de la main-d'œuvre", key="check4")
if check_4:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
    

st.subheader("2/ Lequel des éléments suivants n'est PAS un type courant de données sur la main-d'œuvre collectées pendant la phase d'analyse ?")

check_5 = st.checkbox("a) Données démographiques des employés", key="check5")
if check_5:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_6 = st.checkbox("b) Scores de satisfaction client", key="check6")
if check_6:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
check_7 = st.checkbox("c) Mesures de performances", key="check7")
if check_7:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_8 = st.checkbox("d) Informations sur la rémunération et les avantages sociaux", key="check8")
if check_8:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################


st.subheader("1/ Quelle est l'intérêt d’identifier des indicateurs clés de performance (KPI) dans l’analyse des effectifs ?")

check_9 = st.checkbox("a) Les KPI sont utilisés pour les promotions des employés.")

if check_9:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_10 = st.checkbox("b) Les KPI fournissent une mesure de la satisfaction des employés.")

if check_10:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_11 = st.checkbox("c) Les KPI aident à mesurer les performances de la main-d'œuvre par rapport aux objectifs stratégiques.")

if check_11:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_12 = st.checkbox("d) Les KPI sont principalement utilisés à des fins d’analyse comparative externe.")

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
redirect_button("https://gpec-gepp.streamlit.app/Chapitre_3_🔖_Prévoir_les_besoins_en_talents","Aller au chapitre 3")



