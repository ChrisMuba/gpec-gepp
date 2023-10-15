


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Chapitre 3")

st.sidebar.markdown("# Chapitre 3")

st.title("Prévoir les besoins en talents")

st.markdown("Prédire les futurs besoins en talents est un aspect crucial de la planification stratégique des effectifs. Cela implique d’anticiper les aptitudes, les rôles et les compétences dont une organisation aura besoin pour atteindre ses objectifs stratégiques.") 

st.markdown("Ce chapitre explore diverses méthodes et stratégies pour prévoir les besoins en talents.") 

st.markdown("")

if st.button("Cliquez pour acceder au Chap.2 - **A/ Méthodes de prévision des besoins futurs en main-d’œuvre**"):
    
    st.subheader("📈Chap.2-A/ Prévision des besoins futurs📉")
    
    
    st.markdown("Les méthodes de prévision peuvent inclure:") 
    
    st.markdown("- **Analyse des données historiques** : l'examen des données historiques sur la main-d'œuvre, telles que les taux de rotation, les promotions et les tendances de recrutement, peut fournir un aperçu des futurs besoins en talents. Cette méthode est utile pour identifier des modèles récurrents.") 
    
    st.markdown("- **Analyse des tendances** : l'examen des tendances du secteur et des forces du marché peut aider à prédire les besoins futurs en main-d'œuvre. Par exemple, si une nouvelle technologie est sur le point de perturber votre secteur, vous devrez peut-être prévoir les besoins en talents pour les compétences connexes.")

    st.markdown("- **Projections de croissance** : il est essentiel d’aligner les besoins en talents avec les projections de croissance de l’entreprise. Si votre organisation envisage de se développer sur de nouveaux marchés ou de lancer de nouveaux produits, vous devrez probablement embaucher des talents supplémentaires.")

    st.markdown("- **Planification de la succession** : identifier et développer les talents internes pour des rôles clés est un moyen proactif de prévoir les besoins en talents. En évaluant l’état de préparation de vos employés à accéder à des postes à responsabilités, vous pouvez réduire le recours au recrutement externe.")

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

    
    



        
        
        
        
        
        
