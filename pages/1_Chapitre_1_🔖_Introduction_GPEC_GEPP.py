#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

import pandas as pd

st.markdown("# Chapitre 1")
st.sidebar.markdown("# Chapitre 1")

st.title("Introduction à la GPEC, GEPP et à la planification stratégique")

st.markdown("La **GPEC** (Gestion Prévisionnelle des Emplois et des Compétences) et la **GEPP** (Gestion des Emplois et des Parcours Professionnels) sont deux démarches de GRH qui visent à anticiper les besoins futurs en compétences et en effectifs au sein d'une organisation.")

st.markdown("Alors que la :blue[GPEC] est une démarche plus globale qui vise à mettre en adéquation les effectifs, les emplois et les compétences avec les objectifs stratégiques et l'environnement externe de l'entreprise ; La :blue[GEPP] va être une démarche plus focalisée sur les parcours professionnels des salariés actuels de l'entreprise. Elle visera à favoriser l'évolution professionnelle des salariés en fonction de leurs compétences et de leurs aspirations.")

st.markdown("")

if st.button("Cliquez pour acceder au Chap.1 - **A/ Étapes de la GPEC et de la GEPP**"):
    st.subheader("📗Chap.1-A/ Étapes de la GPEC et de la GEPP📘")

    st.subheader("Etapes de la :blue[GPEC] :")
    
    st.markdown("- **Analyse de l'environnement** : analyse des évolutions économiques, technologiques, sociales et démographiques qui impacteront les besoins futurs en compétences.")
    st.markdown("- **Évaluation des emplois** : identification des compétences et des connaissances nécessaires pour chaque emploi.")
    st.markdown("- **Planification des effectifs** : anticipation des besoins futurs en effectifs en fonction des évolutions des emplois.")
    st.markdown("- **Développement des compétences** : mise en place des actions de formation et de développement des compétences pour adapter les salariés aux besoins futurs.")
    
    st.markdown("")

    st.subheader("Etapes de la :blue[GEPP] :")
    
    st.markdown("- **Accompagnement des parcours professionnels** : mise en place des outils et des dispositifs pour identifier les compétences des salariés et accompagner la construction de leurs parcours professionnels.")
    st.markdown("- **Développement des compétences** : proposition des actions de formation et de développement des compétences pour aider les salariés à évoluer professionnellement.")
    st.markdown("- **Planification des effectifs** : favorisation de la mobilité professionnelle des salariés au sein de l'entreprise ou vers l'extérieur.")


# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/take_notes.gif')

if st.button("Continuer vers la suite du Chap.1 - **B/ Planification stratégique**"):
    
    st.subheader("📗Chap.1-B/ Planification stratégique📘")

    st.markdown("**A/ Introduction à la planification stratégique de la main-d'œuvre**")

    st.markdown("La :blue[planification stratégique des effectifs] est un aspect crucial de la gestion moderne des RH. Il s'agit d'un processus systématique et axé sur les :blue[données] qui garantit que la main-d'œuvre d'une organisation est alignée sur ses objectifs stratégiques et ses buts futurs. Dans un paysage d'entreprise en constante évolution, où les talents sont une ressource précieuse, la planification stratégique des effectifs permet aux RH de relever de manière proactive les problèmes de la main-d'œuvre, d'optimiser l'utilisation des talents et de se préparer pour l'avenir.")

    st.markdown("")
    
    st.markdown("**B/ Qu'est-ce que la planification stratégique de la main-d'œuvre**")
    
    st.markdown("La planification stratégique de la main-d'œuvre peut être définie comme un processus actif d'**analyse**, de **prévision** et d'**alignement des effectifs** d'une organisation pour atteindre ses buts et objectifs stratégiques.") 
    
    st.markdown("Elle va au-delà des fonctions traditionnelles des RH et se concentre sur la situation dans son ensemble. La planification stratégique de la main-d'œuvre consiste à **comprendre les effectifs actuels d'une organisation, à évaluer ses capacités et à anticiper les compétences et les talents nécessaires pour assurer le succès futur de l'entreprise**.") 
    
    st.markdown("En substance, **la planification stratégique vise à faire en sorte qu'une organisation ait les bonnes personnes au bon endroit au bon moment**.")

    st.markdown("")
    
    
if st.button("Continuer vers la suite du Chap.1 - **C/ Rôle des RH dans la planification stratégique**"):
    
    st.subheader("📗Chap.1-C/ RH et planification stratégique📘")
    
    st.markdown("**Historiquement, les RH étaient considérées avant tout comme une fonction administrative**, responsable du recrutement, de la formation et de la gestion du personnel.") 
    
    st.markdown("Toutefois, dans l'environnement concurrentiel d'aujourd'hui, les RH sont devenues un **partenaire stratégique** au sein des organisations. Les RH ne sont plus confinés aux questions de routine du personnel; ils jouent un rôle essentiel dans l'élaboration de la stratégie globale de l'entreprise.") 
    
    st.markdown("La planification stratégique de la main-d'œuvre témoigne de cette transformation, car elle place les ressources humaines au cœur de la prise de décisions stratégiques.") 

    st.markdown("Le rôle des RH dans la planification stratégique consiste à: : ") 
                
    st.markdown("- **Identifier et accompagner les talents** : identifier les employés à fort potentiel, leur offrir des possibilités de développement pour des rôles futurs au sein de l'entreprise.") 

    st.markdown("- **Remédier aux faiblesses de la main-d'œuvre** : identifier les déficits de compétences et les excédents au sein de l'organisation et élaborer des stratégies pour combler ces lacunes, que ce soit par le recrutement, la formation ou la planification de la relève.")

    st.markdown("- **Assurer l'alignement aux buts stratégiques** : veiller à ce que les effectifs de l'organisation soient alignés sur ses buts et objectifs stratégiques. Cet alignement est essentiel pour assurer le succès des entreprises.")
    
    st.markdown("")
    
    
if st.button("Continuer vers Chap.1 - **D/ Lier la planification de la main-d'œuvre à la stratégie commerciale**"):
    
    st.subheader("📗Chap.1-D/ Planification et Stratégie commerciale📘")

    st.markdown("La planification stratégique de la main-d'œuvre n'est pas un processus autonome; elle est étroitement liée à la stratégie d'entreprise d'une organisation. Elle veille à ce que le capital humain d'une organisation appuie et encourage l'exécution du plan stratégique.") 
    
    st.markdown("Le lien entre la planification stratégique de la main-d'œuvre et la stratégie d'entreprise est un lien dynamique, où les RH travaillent en collaboration avec la Direction pour traduire les objectifs de l'entreprise en planification réalisable de la main-d'œuvre.")

    st.markdown("Ce lien est essentiel pour plusieurs raisons :")

    st.markdown("- **Agilité** : La planification stratégique permet à une organisation de s'adapter rapidement aux changements de l'environnement extérieur, aux tendances de l'industrie et à l'évolution des demandes des clients. Une main-d'œuvre souple peut être restructurée pour relever de nouveaux défis et de nouvelles opportunités.")

    st.markdown("- **Efficacité, rentabilité** : Lorsque la main-d'œuvre est stratégiquement planifiée, les ressources sont allouées de manière efficace, ce qui réduit les dépenses inutiles liées à l'embauche, à la formation et au renouvellement du personnel.")

    st.markdown("- **Avantage concurrentiel** : Une main-d'œuvre bien alignée peut être une source d'avantage concurrentiel, car elle soutient la proposition de valeur unique de l'organisation et l'aide à se démarquer sur le marché.")

    st.markdown("")
    
    st.markdown("La planification stratégique de la main-d'œuvre est donc une pratique essentielle car elle donne les outils et les connaissances nécessaires pour aligner la main-d'œuvre sur les objectifs stratégiques d'une organisation.") 
    
    st.markdown("En comprenant l'importance de la planification stratégique et son lien avec la stratégie d'entreprise, les RH peuvent stimuler le succès organisationnel, favoriser l'innovation et donc aider l'organisation à rester compétitive dans un paysage dynamique et concurrentiel.")
    
                
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
    redirect_button("https://gpec-gepp.streamlit.app/Quiz_1_-_Introduction_GPEC_GEPP","Quiz du chapitre 1")


                
    



    
   




    



    



