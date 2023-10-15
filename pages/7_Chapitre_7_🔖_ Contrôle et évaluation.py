


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Chapitre 7")

st.sidebar.markdown("# Chapitre 7")

st.title("Contrôle et évaluation")

st.markdown("Un suivi et une évaluation efficaces sont des éléments essentiels de la planification stratégique des effectifs. Ils veillent à ce que le plan soit sur la bonne voie, adaptable aux circonstances changeantes et contribuant aux objectifs stratégiques de l'organisation.") 


st.markdown("")

if st.button("Cliquez pour acceder au Chap.7 - **A/ Indicateurs et mesures de performance**"):
    
    st.subheader("📗Chap.7-A/ Indicateurs et mesures de performance📘")
    
    st.markdown("") 
    
    st.markdown("- **Sélection des KPI pertinents** : choisissez des KPI qui correspondent aux objectifs stratégiques et aux buts de la planification stratégique. Ces KPI doivent refléter les résultats qui comptent le plus pour l'organisation.") 
    
    st.markdown("- **Établir des références** : créez des mesures de référence pour chaque KPI. Ces repères servent de point de référence par rapport auquel vous pouvez comparer les progrès.")

    st.markdown("- **Collecte régulière de données** : collectez régulièrement des données pour suivre les performances de la main-d'œuvre et son alignement avec la planification stratégique.")

    st.markdown("- **Analyse des données** : analysez les données collectées pour identifier les tendances, les domaines d'amélioration et les problèmes potentiels. Recherchez des corrélations et des modèles qui fournissent des informations sur l’efficacité de la main-d’œuvre.")

    st.markdown("- **Génération de rapports** : développez des rapports clairs et concis qui présentent les résultats de votre analyse. Ces rapports doivent être partagés avec les parties prenantes concernées.")

                            
    st.markdown("")
    
        
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/take_notes.gif')

if st.button("Continuer vers la suite du Chap.7 - **B/ Examens et ajustements périodiques des effectifs**"):
    
    st.subheader("📗Chap.7-B/ Examens et ajustements des effectifs📘")
    
    
    st.markdown("- **Examens programmés** : effectuer des examens périodiques des progrès de la planification stratégique. Ces examens peuvent être mensuels, trimestriels ou déterminés par les besoins spécifiques de votre organisation.")

    st.markdown("- **Collaboration interfonctionnelle** : impliquez les parties prenantes de divers départements, y compris les ressources humaines, la direction et les supérieurs hiérarchiques, dans le processus d'examen. Cela garantit une perspective holistique.")

    st.markdown("- **Comparaison des résultats réels et prévus** : comparez les performances réelles par rapport aux objectifs et aux KPI prévus. Identifiez les lacunes ou les domaines dans lesquels des ajustements sont nécessaires.")

    st.markdown("- **Planification de scénarios** : envisagez divers scénarios et leur impact potentiel sur la main-d'œuvre. Planifiez les imprévus et les stratégies alternatives en fonction de vos découvertes.")

    st.markdown("- **Stratégies d'ajustement** : si nécessaire, élaborer des stratégies pour résoudre les problèmes et les lacunes identifiés lors de l'examen. Ces stratégies peuvent inclure des changements dans l'embauche, la formation ou d'autres activités de développement de la main-d'œuvre.")

    
    st.markdown("")


if st.button("Continuer vers la suite du Chap.7 - **C/ Évaluation de l'efficacité du plan**"):
    
    st.subheader("📗Chap.7-C/ Évaluation de l'efficacité du plan📘")
    
    
    st.markdown("- **Commentaires des parties prenantes** : Sollicitez les commentaires des employés, des gestionnaires et des autres parties prenantes impliquées dans la mise en œuvre de la planification stratégique. Leur contribution peut fournir des informations précieuses sur l’efficacité du plan.")

    st.markdown("- **Évaluation de l'impact** : évaluer l'impact de la planification stratégique sur la capacité de l'organisation à atteindre ses objectifs stratégiques. Tenez compte de l'influence du plan sur la productivité, la rentabilité et le développement des talents.")

    st.markdown("- **Analyse coûts-avantages** : évaluer si les avantages de la planification stratégique dépassent les coûts associés à sa mise en œuvre. Cette analyse doit prendre en compte à la fois les facteurs financiers et non financiers.")

    st.markdown("- **Apprendre des réussites et des échecs** : identifiez les aspects de la planification stratégique qui ont été couronnés de succès et les domaines dans lesquels des améliorations sont nécessaires. Utilisez ces informations pour affiner votre approche.")

    st.markdown("- **Amélioration continue** : intégrer les leçons tirées du processus d'évaluation dans les futures itérations de la planification stratégique. Cela garantit que le plan évolue et reste pertinent au fil du temps.")
                
    st.markdown("")

    st.markdown("Un suivi et une évaluation efficaces aident non seulement les organisations à maintenir leur planification stratégique sur la bonne voie, mais leur permettent également de s'adapter aux changements et d'améliorer l'efficacité du plan au fil du temps.") 
    
    st.markdown("En évaluant et en ajustant régulièrement le plan, les organisations peuvent maintenir un effectif aligné sur leurs objectifs stratégiques et qui reste agile face à l'évolution des défis et des opportunités.")

    st.markdown("")

    

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
    redirect_button("https://gpec-gepp.streamlit.app/Quiz_7_-_Contrôle_et_évaluation","Quiz du chapitre 7")

    
    



        
        
        
        
        
        
