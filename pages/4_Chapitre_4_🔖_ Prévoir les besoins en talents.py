


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Chapitre 4")

st.sidebar.markdown("# Chapitre 4")

st.title("Segmentation et analyse de l’offre de main-d’œuvre")

st.markdown("Pour garantir que la main-d'œuvre de votre organisation s'aligne sur ses objectifs stratégiques, il est essentiel de segmenter la main-d'œuvre en fonction des rôles et des compétences critiques requis pour réussir. De plus, l’analyse de l’offre de main-d’œuvre, tant en interne qu’en externe, est cruciale pour répondre de manière proactive aux besoins en talents. Ce chapitre explore ces aspects ainsi que l’importance de la planification de la relève et des réserves de talents.") 

st.markdown("")

if st.button("Cliquez pour acceder au Chap.2 - **A/ Catégoriser la main-d'œuvre en fonction des rôles critiques**"):
    
    st.subheader("📈Chap.2-A/ Catégoriser en fonction des rôles critiques📉")
    

    st.markdown("La segmentation de la main-d'œuvre implique de classer les employés en différentes catégories en fonction de leurs rôles, compétences et contributions à l'organisation. Lorsqu’il s’agit de planification stratégique des effectifs, la catégorisation est essentielle pour concentrer les ressources et les efforts là où elles sont le plus nécessaires.")
    
    st.markdown("Les étapes clés de la catégorisation de la main-d’œuvre comprennent :") 

    st.markdown("- **Définition des catégories** : déterminez les catégories ou les segments au sein de votre organisation en fonction de l'importance des rôles et des compétences. Par exemple, identifiez les rôles critiques, clés et de support.") 
    
    st.markdown("- **Analyse des rôles** : évaluer l'impact stratégique de chaque rôle sur les objectifs de l'organisation. Les rôles critiques sont ceux qui influencent de manière significative la réalisation des objectifs stratégiques.")

    st.markdown("- **Aptitudes et compétences** : identifiez les compétences clés requises pour chaque catégorie, car différents rôles peuvent nécessiter des ensembles de compétences distincts.")

    st.markdown("- **Allocation des ressources** : allouez des ressources, telles que la formation, le recrutement ou le développement des talents, en fonction de l'importance stratégique de chaque catégorie.")

    st.markdown("")

    st.markdown("La catégorisation de la main-d'œuvre garantit que l'orientation stratégique et les ressources sont orientées vers les rôles qui ont l'impact le plus significatif sur le succès de votre organisation.")

    st.markdown("")

    

        
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/take_notes.gif')

if st.button("Continuer vers la suite du Chap.2 - **B/ Planification de scénarios et modélisation de la main-d'œuvre**"):
    
    st.subheader("📈Chap.2-B/ Planification de scénarios et modélisation📉")
    
    st.markdown("La planification de scénarios implique la création de différents scénarios futurs et l’évaluation de leur impact sur les besoins de main-d’œuvre. Cette méthode peut être utilisée pour se préparer à diverses situations potentielles.") 
    
    st.markdown("La modélisation des effectifs complète la planification de scénarios en fournissant une vue détaillée de la manière dont les changements d’effectifs affectent l’organisation.") 
    
    st.markdown("Les étapes de la planification de scénarios et de la modélisation des effectifs comprennent :") 
    
    st.markdown("- **Création de scénarios** : développez plusieurs scénarios basés sur différentes hypothèses, telles que les conditions économiques, la dynamique du marché ou les progrès technologiques.")

    st.markdown("- **Impacts sur la main-d'œuvre** : évaluez l'impact de chaque scénario sur les besoins en main-d'œuvre, notamment l'embauche, les licenciements, le perfectionnement des compétences ou autre réorganisation.")

    st.markdown("- **Allocation des ressources** : déterminez les ressources nécessaires pour prendre en charge chaque scénario et hiérarchisez-les en fonction de leur importance stratégique.")

    st.markdown("- **Atténuation des risques** : développer des stratégies pour atténuer les risques associés à chaque scénario et garantir que la main-d'œuvre reste agile.")

    st.markdown("")

    st.markdown("La planification de scénarios et la modélisation des effectifs va aider les organisations à se préparer à un large éventail d’avenirs potentiels et à garantir que les besoins en talents correspondent à ces possibilités.")

    st.markdown("")


if st.button("Continuer vers la suite du Chap.2 - **C/ Identifier les rôles et compétences critiques**"):
    
    st.subheader("📈Chap.2-C/ Identifier rôles et compétences critiques📉")
    
    st.markdown("Tous les rôles ne sont pas égaux en termes d’importance stratégique. L’identification des rôles et des compétences critiques est essentielle pour une planification stratégique efficace.") 
    
    st.markdown("Voici comment procéder :") 
    
    st.markdown("- **Objectifs stratégiques** : commencez par comprendre les objectifs stratégiques de votre organisation. Quels rôles et compétences sont les plus cruciaux pour atteindre ces objectifs ?")

    st.markdown("- **Cartographie des compétences** : créez un cadre de compétences qui décrit les compétences et les connaissances requises pour chaque rôle. Identifiez les compétences essentielles à votre mission.")

    st.markdown("- **Analyse d'impact** : évaluez l'impact du fait de ne pas avoir les bonnes personnes dans ces rôles critiques. Cela pourrait inclure des implications financières, opérationnelles ou stratégiques.")

    st.markdown("- **Planification de la relève** : élaborer des stratégies pour garantir un vivier de talents pour ces rôles. Cela peut impliquer la préparation de candidats internes, un recrutement stratégique ou des partenariats avec des établissements d'enseignement.")

    st.markdown("")

    st.markdown("L'identification des rôles et des compétences critiques garantit que vos efforts de planification stratégique des effectifs sont concentrés sur les domaines qui ont l'influence la plus significative sur le succès de votre organisation.")

    st.markdown("")

    st.markdown("En conclusion, la prévision des besoins en talents est un élément clé de la planification stratégique des effectifs. En utilisant des méthodes basées sur les données, la planification de scénarios et la modélisation de la main-d'œuvre, et en identifiant les rôles et compétences critiques, les RH peuvent garantir que leur organisation est prête à répondre aux futures demandes de main-d'œuvre et aux objectifs stratégiques.")

    

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
    redirect_button("https://gpec-gepp.streamlit.app/Quiz_3_-_Pr%C3%A9voir_les_besoins_en_talents📉","Quiz du chapitre 3")

    
    



        
        
        
        
        
        
