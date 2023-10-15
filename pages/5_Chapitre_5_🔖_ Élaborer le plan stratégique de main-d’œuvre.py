


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Chapitre 5")

st.sidebar.markdown("# Chapitre 5")

st.title("Élaborer le plan stratégique de main-d’œuvre")

st.markdown("L'élaboration d'un plan stratégique est une phase cruciale dans le processus d'alignement de la main-d'œuvre de votre organisation sur ses buts et objectifs stratégiques. À cette étape, vous traduisez les intentions stratégiques en stratégies RH exploitables qui garantiront que votre personnel est adéquatement équipé et préparé pour atteindre ces objectifs.") 

st.markdown("")

if st.button("Cliquez pour acceder au Chap.5 - **A/ Définir les objectifs et les buts stratégiques**"):
    
    st.subheader("📗Chap.5-A/ Définir les objectifs et les buts stratégiques📘")
    
    
    st.markdown("La planification stratégique commence par une compréhension claire des objectifs et buts stratégiques de votre organisation. Ce sont les piliers fondamentaux sur lesquels sera construit le plan de main-d’œuvre.")
    
    st.markdown("Les étapes de définition des objectifs et buts stratégiques comprennent :") 
    
    
    st.markdown("- **Alignement stratégique** : veiller à ce que les objectifs de la planification stratégique s'alignent étroitement sur les objectifs stratégiques globaux de l'organisation.") 
    
    st.markdown("- **Clarté des objectifs** : définissez clairement ce que votre organisation vise à réaliser à court et à long terme.")

    st.markdown("- **Indicateurs clés de performance (KPI)** : spécifiez les KPI qui seront utilisés pour mesurer les progrès et succès dans la réalisation des objectifs stratégiques.")

    st.markdown("- **Allocation des ressources** : Déterminer les ressources nécessaires, tant en termes de budget que de capital humain, pour soutenir ces objectifs.")

    st.markdown("")
    

        
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/take_notes.gif')

if st.button("Continuer vers la suite du Chap.5 - **B/ Créer des plans d'action pour combler déficits de talents**"):
    
    st.subheader("📗Chap.5-B/ Créer des plans d'action pour combler déficits de talents📘")
    
    
    st.markdown("Une fois les objectifs et buts stratégiques définis, l’étape suivante consiste à créer des plans d’action pour combler les déficits de talents susceptibles d’entraver la réalisation de ces objectifs.")  
    
    st.markdown("Cela comprend les étapes suivantes :") 
    
    st.markdown("- **Analyse des écarts de compétences** : reportez-vous aux résultats de votre analyse des écarts de compétences pour identifier les domaines spécifiques dans lesquels votre main-d'œuvre ne possède pas les aptitudes et compétences requises.")

    st.markdown("- **Développement et formation** : élaborer des plans de formation et de développement pour les employés existants afin de combler ces lacunes en matière de compétences.")

    st.markdown("- **Stratégies de recrutement** : Élaborer des stratégies de recrutement de nouveaux talents afin de remédier aux pénuries de compétences qui ne peuvent être comblées par le développement interne.")

    st.markdown("- **Planification des promotions et de la succession** : mettre en œuvre des plans de promotion et de succession pour préparer les candidats internes à des rôles clés.")

    st.markdown("- **Gestion des performances** : mettre en œuvre un système de gestion des performances qui aligne les objectifs individuels avec les objectifs organisationnels, favorisant ainsi une culture de responsabilité.")

    st.markdown("")

    st.markdown("")


if st.button("Continuer vers la suite du Chap.5 - **C/ Stratégie d’acquisition et de rétention des talents**"):
    
    st.subheader("📗Chap.5-C/ Stratégie d’acquisition et de rétention des talents📘")
    
    st.markdown("L'acquisition et la rétention des meilleurs talents sont une partie essentielle du processus de planification stratégique. L’élaboration d’une solide stratégie d’acquisition et de rétention des talents comprend les éléments clés suivants :") 
    
    st.markdown("- **Marque employeur** : Créer et promouvoir une marque employeur attractive qui séduit les candidats à haut potentiel.")

    st.markdown("- **Recrutement et sélection** : développez des processus de recrutement et de sélection efficaces pour identifier et embaucher les candidats les mieux adaptés à votre organisation.")

    st.markdown("- **Intégration** : mettre en œuvre un processus d'intégration structuré pour faciliter une transition en douceur pour les nouvelles recrues.")

    st.markdown("- **Rémunération et avantages** : Concevoir des programmes de rémunération et des avantages sociaux compétitifs pour attirer et retenir les meilleurs talents.")

    st.markdown("- **Développement de carrière** : fournir des voies claires pour le développement de carrière au sein de l'organisation, en présentant des opportunités à long terme.")

    st.markdown("- **Équilibre travail-vie personnelle** : Promouvoir l’équilibre travail-vie personnelle et un environnement de travail sain pour améliorer la rétention des employés.")

    st.markdown("- **Engagement des employés** : mettre en œuvre des stratégies pour favoriser l'engagement des employés, telles que des mécanismes de rétroaction, des programmes de reconnaissance et des opportunités de participation.")

    st.markdown("- **Planification de la relève** : Développez en permanence un vivier de talents internes prêts à assumer des rôles clés.")

    st.markdown("")

    st.markdown("La stratégie d'acquisition et de rétention des talents doit être étroitement alignée sur les valeurs, la culture et les objectifs stratégiques de l'organisation.")

    st.markdown("")

    st.markdown("En définitive, l'élaboration du plan stratégique en matière de main-d'œuvre implique de traduire les objectifs stratégiques en stratégies RH concrètes. En définissant clairement des objectifs, en créant des plans pour combler les déficits de talents et en élaborant une stratégie d'acquisition et de rétention des talents, les organisations peuvent garantir que leurs effectifs sont alignés sur les objectifs stratégiques et prêts à réussir.")

    

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
    redirect_button("https://gpec-gepp.streamlit.app/Quiz_5_-_Prévoir_les_besoins_en_talents📉","Quiz du chapitre 5")

    
    



        
        
        
        
        
        
