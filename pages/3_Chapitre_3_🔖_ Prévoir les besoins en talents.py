


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Chapitre 3")

st.sidebar.markdown("# Chapitre 3")

st.title("Prévoir les besoins en talents")

st.markdown("Prédire les futurs besoins en talents est un aspect crucial de la planification stratégique des effectifs. Cela implique d’anticiper les aptitudes, les rôles et les compétences dont une organisation aura besoin pour atteindre ses objectifs stratégiques.") 

st.markdown("Ce chapitre explore diverses méthodes et stratégies pour prévoir les besoins en talents.") 

st.markdown("")

if st.button("Cliquez pour acceder au Chap.2 - **A/ Méthodes de prévision des besoins futurs en main-d’œuvre**"):
    
    st.subheader("📈Chap.2-A/ Prévision des besoins futurs en main-d’œuvre📉")
    
    
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


if st.button("Continuer vers la suite du Chap.2 - **C/ Réaliser une analyse des écarts de compétences**"):
    
    st.subheader("📈Chap.2-C/ Analyse des écarts de compétences📉")
    
    st.markdown("Une analyse des écarts de compétences est un processus systématique d'évaluation des aptitudes, des connaissances et des compétences de votre main-d'œuvre par rapport aux compétences requises pour atteindre vos objectifs stratégiques.") 
    
    st.markdown("Cette analyse vous aide à identifier les pénuries de compétences et guide vos efforts pour y remédier. Les étapes impliquées dans la réalisation d’une analyse des déficits de compétences comprennent :")
    
    st.markdown("- **Définir les compétences requises** : écrivez clairement les aptitudes et les compétences requises pour atteindre vos objectifs stratégiques.")

    st.markdown("- **Évaluez les compétences actuelles** : évaluez les compétences et les capacités existantes de votre main-d'œuvre.")

    st.markdown("- **Identifier les lacunes en matière de compétences** : comparez les compétences requises avec les compétences actuelles, en mettant en évidence les lacunes.")

    st.markdown("- **Élaborer des plans de développement des compétences** : créer des plans de formation et de développement individuels ou en groupe pour combler les lacunes identifiées.")

    st.markdown("")

    st.markdown("Une analyse des déficits de compétences garantit que la main-d'œuvre de votre organisation est prête à répondre aux demandes de l'avenir, vous permettant ainsi d'allouer plus efficacement les ressources à la formation, au recrutement et au développement.")

    st.markdown("")

    st.markdown("En définitive, l’analyse des effectifs et la collecte de données sont en essentielles à une planification stratégique des effectifs réussie. En collectant et en analysant des données, en identifiant des KPI et en effectuant des analyses des lacunes en matière de compétences, il sera possible de prendre des décisions éclairées et garantir que la main-d'œuvre de l'organisation s'aligne sur ses buts et objectifs stratégiques.")

    

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
    redirect_button("https://gpec-gepp.streamlit.app/Quiz_2_-_Analyse_de_la_main-d'œuvre_et_collecte_de_données📉","Quiz du chapitre 2")

    
    



        
        
        
        
        
        
