#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.title("GPEC - GEPP : :blue[Planification stratégique des effectifs]")

st.subheader("Formateur : Christian MUBA.")

st.caption("*Ancien coordinateur apprentissage CFA académique / Académie de Dijon*")

st.caption("*Diplômé des Master Gestion & Master Sciences (IAE Dijon & UB Dijon)*")

st.caption("Vous souhaitez engager une démarche de *GEPP / GPEC* ? Parlons-en 👉🏾 https://www.linkedin.com/in/chris-muba-io 🌐")

# Explanation
with st.expander("✨:blue[Pourquoi ce cours ?]✨"):
    st.write("""
    Êtes-vous un professionnel RH engagé dans un projet de planification stratégique des effectifs ? 
    
    Vous souhaitez aligner la main-d’œuvre de votre organisation sur ses objectifs stratégiques ?

    *Bienvenue dans notre cours sur la planification stratégique des effectifs !*

    Tout d'abord laissez-moi vous donner 3 raisons principales pour lesquelles la planification stratégique des effectifs est indispensable :

    1️⃣ Elle aligne la stratégie en talents avec la stratégie de l'entreprise : en prévoyant les besoins et les tendances en matière de main-d'œuvre, vous pouvez constituer de manière proactive la main-d'œuvre nécessaire pour atteindre les objectifs de l'organisation.

    2️⃣ Elle devance les pénuries de talents : la planification des effectifs permet d'anticiper les situations où des pénuries de compétences pourraient survenir et permet aussi de développer des solutions avant qu'elles n'aient un impact sur les différentes activités de  l'organisation.

    3️⃣ Elle éclaire la prise de décisions en matière de talents : grâce à des informations basées sur les données de l'offre et la demande, il est possible d'investir de façon plus intelligente dans le recrutement, le développement et la fidélisation des talents.

    
    💡Notre cours en ligne propose une approche complète et pratique pour élaborer une stratégie efficace en matière de main-d'œuvre.


    Les apprenants acquerront une :blue[compréhension approfondie] des meilleures pratiques pour analyser le personnel actuel 📊, projeter les besoins futurs 🔮 et développer des solutions pour combler les écarts en matière de talents. 
    
    Grâce à des exercices interactifs et des exemples concrets, les participants apprendront comment évaluer l'offre et la demande de main-d'œuvre, identifier les excédents et les pénuries de talents, mettre en œuvre des programmes de recrutement et de développement 👩‍🏫 et créer un tableau de bord 📈 pour suivre les progrès.

    À la fin du cours, les professionnels des RH seront équipés pour s'associer aux dirigeants et planifier une main-d'œuvre qui stimule le succès organisationnel, aujourd'hui et à l'avenir ⏩. Ils auront une vision claire du plan stratégique de main-d'œuvre adapté aux besoins et objectifs spécifiques de leur organisation 🎯.

    Le cours est régulièrement mis à jour pour refléter les dernières tendances, technologies et meilleures pratiques qui influencent la main-d'œuvre 👥. 
    
    Que vous soyez un professionnel RH cherchant à perfectionner ses compétences ou cherchant à faire progresser votre carrière, ce cours vous fournira les compétences nécessaires pour faire de la planification stratégique des effectifs une capacité essentielle. 💪

    
    

    Ne laissez pas la planification stratégique des effectifs devenir un défi de taille. Dotez-vous des compétences nécessaires pour prendre des décisions RH éclairées qui profitent à votre organisation.
    

    **Prêt à vous lancer dans votre voyage vers l’excellence RH basée sur les données ?** :blue[Commencez le cours maintenant et améliorez vos compétences en planification stratégique des effectifs !]
    """)

st.subheader("Description du cours")

st.markdown("Ce cours pratique est conçu pour doter les professionnels des RH des connaissances et des compétences requises pour une planification stratégique efficace des effectifs. Les participants apprendront à aligner les effectifs de leur organisation sur ses objectifs stratégiques, à analyser les besoins actuels et futurs en talents et à élaborer des stratégies pour combler les faiblesses en matière de main-d'œuvre.")

st.subheader("🚀Objectifs d'apprentissage🚀")

st.markdown("À la fin de ce cours, les participants devraient être capables de :")

st.markdown("🎯Comprendre le concept et l'importance de la planification stratégique des effectifs en RH.")
st.markdown("🎯Effectuer une analyse approfondie de la main-d’œuvre actuelle et identifier les forces et les faiblesses.")
st.markdown("🎯Alignez la planification des effectifs avec les objectifs stratégiques de l’organisation.")
st.markdown("🎯Élaborer un plan stratégique en matière de main-d’œuvre pour combler les manques et les excédents de talents.")
st.markdown("🎯Mettre en œuvre, surveiller et évaluer l’efficacité du plan stratégique en matière de main-d’œuvre.")
st.markdown("🎯Anticiper et s’adapter à l’évolution des tendances et des défis en matière de main-d’œuvre.")

with st.sidebar:
    st.image('GIF/fusee.gif')


st.markdown("")


st.markdown("")


# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")


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
redirect_button("https://gpec-gepp.streamlit.app/Chapitre_1_🔖_Introduction_GPEC_GEPP","Aller au chapitre 1")



# In[ ]:





# In[ ]:




