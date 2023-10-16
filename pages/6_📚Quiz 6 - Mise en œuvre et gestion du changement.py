



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 6")
st.sidebar.markdown("# Quiz du chapitre 6")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/analyze_this.gif')

st.title("Statistiques descriptives")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours de **Statistiques descriptives**.")

st.markdown("Cocher les bonnes réponses.")

st.header("A/ Mesures de tendance centrale")

st.subheader("1/ Laquelle des mesures de tendance centrale suivantes est la plus couramment utilisée pour résumer des montants de salaires ?")

check = st.checkbox("a) Mode", key="check1")
if check:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_2 = st.checkbox("b) Médiane", key="check2")
if check_2:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_3 = st.checkbox("c) Moyenne géométrique", key="check3")
if check_3:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_4 = st.checkbox("d) Moyenne arithmétique", key="check4")
if check_4:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
    

st.subheader("2/ Quelle mesure de tendance centrale est la plus appropriée à utiliser lorsque les données incluent des valeurs aberrantes fortement asymétriques")

check_5 = st.checkbox("a) Mode", key="check5")
if check_5:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_6 = st.checkbox("b) Médiane", key="check6")
if check_6:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
check_7 = st.checkbox("c) Moyenne arithmétique", key="check7")
if check_7:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_8 = st.checkbox("d) Moyenne géométrique", key="check8")
if check_8:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################


st.subheader("3/ Quelle est la formule pour calculer la variance d'un échantillon ?")

check_9 = st.checkbox("a) somme des écarts à la moyenne / taille de l'échantillon")

if check_9:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_10 = st.checkbox("b) somme des carrés des écarts à la moyenne / taille de l'échantillon")

if check_10:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_11 = st.checkbox("c) somme des carrés des écarts à la moyenne / (taille de l'échantillon - 1) ")

if check_11:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_12 = st.checkbox("d) somme des écarts à la moyenne / (taille de l'échantillon taille - 1)")

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




