


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Chapitre 2")
st.sidebar.markdown("# Chapitre 2")

st.title("Analyse de la main-d'œuvre et collecte de données")

st.markdown("Une planification efficace des effectifs stratégiques de la main-d'œuvre commence par une **analyse complète des effectifs actuels** de votre organisation. Cette analyse implique la collecte et l'évaluation de données pour mieux comprendre les compétences, les performances et le potentiel de vos employés.") 

st.markdown("Il s'agit d'une **étape critique pour comprendre les forces, les faiblesses et les domaines de votre organisation qui doivent être améliorés**.") 

st.markdown("Ce chapitre décrit les principaux éléments de l'analyse des effectifs et de la collecte de données.") 

st.markdown("")

if st.button("Cliquez pour acceder au Chap.2 - **A/ Collecte et analyse des données de la main-d'œuvre**"):
    
    st.subheader("📈Chap.2-A/ Collecte et analyse des données📉")
    
    st.markdown("**Les données constituent le fondement de l'analyse des effectifs**. Les RH doivent collecter et analyser divers types de données pour avoir une **vue d'ensemble de la main-d'œuvre**.") 
    
    st.markdown("Ces données peuvent inclure:") 
    
    st.markdown("- **Information démographique** : Données sur l'âge, le genre et d'autres facteurs démographiques qui peuvent fournir des informations sur la composition de la main-d'œuvre.") 
    
    st.markdown("- **Compétences et qualifications des employés** : Informations sur la formation, les certifications et les qualifications des employés, qui aident à évaluer les niveaux et le potentiel de compétences.")

    st.markdown("- **Métriques de performance** : Données sur les performances individuelles et en équipe, y compris les principaux indicateurs de performance (KPI) et les paramètres de mesure pertinents pour chaque rôle.")

    st.markdown("- **Données sur le turnover et la rétention des talents** : informations sur les taux de rotation du personnel, les raisons de départ et les stratégies de fidélisation.")

    st.markdown("- **Données sur l'engagement des employés** : Enquêtes et retour d'information qui évaluent l'engagement, la satisfaction et la motivation des salariés.")

    st.markdown("- **Rémunération et avantages** : Données relatives aux salaires et avantages sociaux qui peuvent aider à déterminer si votre organisation est compétitive sur le marché du travail.")

    st.markdown("")
    
    st.markdown("Une fois les données collectées, il faut les analyser pour identifier les modèles, les tendances et les domaines qui nécessitent une attention particulière.") 
    
    st.markdown("Des outils analytiques, des logiciels et des méthodes statistiques peuvent être utilisés pour donner un sens aux données et tirer des conclusions significatives.")

    st.markdown("Pour en apprendre plus sur l'**analyse de données RH**, vous pouvez suivre notre :blue[**Cours de Statistiques appliquées aux Ressources Humaines**] : ") 

    st.markdown("en cliquant ici ⬇️")
                
    st.link_button("Cours de Statistiques appliquées aux RH", "https://cours-stats-rh.streamlit.app/")

    st.markdown("")

    st.markdown(":blue[**Ou continuer vers la suite du chapitre 2**]")

    st.markdown("en cliquant ici ⬇️")


        
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/take_notes.gif')

if st.button("Continuer vers la suite du Chap.2 - **B/ Détermination des principaux indicateurs de performance**"):
    
    st.subheader("📈Chap.2-B/ Détermination des principaux KPI📉")
    
    st.markdown("Les indicateurs clés de performance (KPI) sont des indicateurs critiques qui mesurent la performance et l'efficacité de votre personnel. L'identification et le suivi des bons indicateurs clés de performance sont essentielles pour prendre des décisions éclairées au cours du processus de planification stratégique de la main-d'œuvre.") 
    
    st.markdown("Les indicateurs clés de performance communs pour l'analyse des effectifs sont les suivants :")
    
    st.markdown("- **Productivité des travailleurs** : Mesure de la production ou de la valeur générée par les employés dans un délai déterminé.")

    st.markdown("- **Satisfaction et engagement des travailleurs** : évaluer le degré de satisfaction et d'engagement des employés au sein de l'organisation.")

    st.markdown("- **Taux de turnover** : suivi du pourcentage d'employés qui quittent l'organisation volontairement ou involontairement.")

    st.markdown("- **Délai de pourvoi** : Mmesurer le temps nécessaire pour pourvoir les postes vacants au sein de l'organisation.")

    st.markdown("- **Lacunes en matière de compétences** : identifier les écarts entre les compétences dont une organisation a besoin et celles que possède son personnel.")

    st.markdown("- **Pipeline de succession** : évaluer l'état de préparation des talents internes à assumer des rôles critiques à l'avenir.")

    st.markdown("")

    st.markdown("La sélection et le suivi des KPI qui correspondent aux objectifs stratégiques de votre organisation sont essentiels pour suivre les progrès et identifier les domaines qui nécessitent une intervention.")

    st.markdown("")


if st.button("Continuer vers la suite du Chap.2 - **C/ Réaliser une analyse des écarts de compétences**"):
    
    st.subheader("📈Chap.2-C/ Analyse des écarts de compétences📉")
    
    st.markdown("Les techniques graphiques sont un moyen puissant de visualiser les données et de les rendre plus faciles à comprendre.") 
    st.markdown("Elles peuvent être utilisées pour communiquer aux parties prenantes des informations complexes de manière claire et concise ; et pour identifier des modèles et des tendances qui peuvent ne pas ressortir des données brutes.")
    st.markdown("Les techniques graphiques à utiliser vont dépendre du type de données : **qualitative** ou **quantitative**.") 


    st.markdown("")


    st.subheader("Données qualitatives")

     
    st.markdown("Les types de graphiques courants pour analyser des data RH **qualitatives** incluent :") 
    

    st.markdown("")
    
    
    st.markdown("- **Diagramme circulaire** : Un diagramme circulaire (Camembert) est un graphique qui représente des **données catégorielles** sous forme de tranches du diagramme. Chaque tranche représente une catégorie et la taille de la tranche est proportionnelle au pourcentage du total.")

    st.markdown("**Cas d’usage** des diagrammes circulaires : Ils peuvent être utilisés pour afficher la répartition des employés entre différents services d'une entreprise, fonctions professionnelles, catégories démographiques, etc...")


    st.markdown("")
    

    st.markdown("**🏀Application 8**")
    st.markdown("Une équipe RH souhaite analyser la répartition des employés dans chaque service. Les données sont présentées dans le diagramme circulaire suivant :")


    import pandas as pd
    
# sample dataset:
    data = {
    'Service': ['Marketing', 'Finance', 'IT', 'RH'],
    'Nombre d\'employés': [100, 75, 50, 25]
    }

    df = pd.DataFrame(data)

    import streamlit as st
    import plotly.express as px

# Load the HR data
    data = {
    'Service': ['Marketing', 'Finance', 'IT', 'RH'],
    'Nombre d\'employés': [100, 75, 50, 25]
    }

    df = pd.DataFrame(data)

# Create a Pie Chart using Plotly
    fig = px.pie(df, values='Nombre d\'employés', names='Service', title='Répartition des employés par service')
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation du diagramme circulaire"):
        st.write("""
    Le diagramme circulaire montre la répartition des employés dans les différents services de l'entreprise. Chaque tranche du diagramme circulaire correspond à un service, tel que Marketing, Finance, IT & RH.
    
    La taille de chaque tranche du diagramme est proportionnelle au pourcentage du nombre total d'employés de ce service par rapport à l'ensemble des salariés de tous les services.
    
    On observe enfin que le service Marketing compte la plus grande proportion d'employés (40 %), suivi du service Finance (30 %), du service IT (20 %) et enfin du service RH (10 %).
    """)


    st.markdown("")


    st.markdown("")


    st.markdown("- **Graphique à barres** : Un graphique à barres est un graphique vertical ou horizontal qui affiche des **données catégorielles**. Des barres sont utilisées pour montrer la fréquence ou l’ampleur de chaque catégorie.")

    st.markdown("**Cas d’usage** des graphiques à barres : Ils peuvent être utilisés pour comparer diverses mesures entre différents services, groupes d'employés ou périodes. Notamment taux d'absentéisme / turnover par services, échelles salariales, notes d'évaluations de performances, participation à la formation. etc...")

    st.markdown("")
    

    st.markdown("**🏀Application 9**")
    st.markdown("Supposons qu'un contrôleur de gestion sociale souhaite analyser les taux d'absentéisme du personnel dans différents services au cours de l'année écoulée. Un graphique à barres peut afficher le taux d'absentéisme (axe des y) pour chaque service (axe des x) afin d'identifier les tendances et les problèmes potentiels.")


    import streamlit as st
    import plotly.express as px

# Load the HR data with colors for each department
    data = {
    'Service': ['RH', 'Finance', 'IT', 'Marketing', 'Ventes'],
    'Taux Absentéisme (%)': [8.5, 5.2, 6.8, 9.3, 7.0],
    }

    df = pd.DataFrame(data)

# Define a color map with department names as keys and colors as values
    color_map = {
    'HR': '#1f77b4',
    'Finance': '#ff7f0e',
    'IT': '#2ca02c',
    'Marketing': '#d62728',
    'Ventes': '#9467bd'
    }

# Create a Bar Graph using Plotly with assigned colors and department names as legend
    fig = px.bar(df, x='Service', y='Taux Absentéisme (%)', title='Taux d\'absentéisme par service',
             color='Service', color_discrete_map=color_map)
    st.plotly_chart(fig)
    
# Explanation
    with st.expander("🔮Interpretation du graphique à barres"):
        st.write("""
    Le graphique à barres représente les taux d'absentéisme dans différents services d'une entreprise au cours de l'année écoulée. Chaque barre du graphique correspond à un service, tel que RH, Finance, IT, Marketing et Ventes.
    
    La hauteur de chaque barre représente le taux d'absentéisme de ce service : nous pouvons voir que le service Marketing a le taux d'absentéisme le plus élevé (9.3 %), suivi par le service RH (8.5), Ventes (7 %), IT (6.8 %) et enfin Finance (5.2 %).
    """)


    st.markdown("")


    st.markdown("")


    st.subheader("Données quantitatives")


    st.markdown("Les types de graphiques courants pour analyser des data RH **quantitatives** incluent :") 


    st.markdown("- **Histogrammes** : Un histogramme est une représentation graphique de la distribution d'un ensemble de **données quantitatives**, où les données sont divisées en un ensemble d'intervalles et le nombre de points de données appartenant à un intervalle est représenté par la hauteur d'une barre.")

    st.markdown("**Cas d’usage** des histogrammes : Ils peuvent être utilisés pour comprendre la distribution d'une seule variable, telle que les salaires des employés, les années d'expérience, etc...")


    st.markdown("")
    

    st.markdown("**🏀Application 10**")
    st.markdown("Imaginez que vous êtes un responsable RH chargé de comprendre la répartition des salaires au sein de votre entreprise. La plupart des employés gagnent-ils des salaires similaires ou disposez-vous d’un large éventail d’échelles salariales ?") 
    st.markdown("Un histogramme peut vous aider à répondre à ces questions et à obtenir des informations précieuses en fournissant une image claire des échelles et fourchettes salariales les plus courantes parmi vos employés.")


    import streamlit as st
    import numpy as np
    import plotly.express as px

# Generate random salary data for 100 employees (in thousands of dollars)
    np.random.seed(42)
    salaries = np.random.normal(50, 10, 100)

# Create a Plotly histogram figure with a custom legend label and no legend title
    fig = px.histogram(salaries, nbins=20, title='Répartition des salaires dans notre entreprise')
    fig.update_xaxes(title_text='Salaire (en milliers d\'€)')
    fig.update_yaxes(title_text='Nombre d\'employés')

# Remove the legend title
    fig.update_layout(legend_title_text='Salaire (€)')

# Displaying Chart
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation de l'histogramme"):
        st.write("""
    Cet histogramme est une représentation graphique de la répartition des salaires entre les salariés de notre entreprise. Chaque barre de l'histogramme correspond à une fourchette salariale spécifique (en milliers d'€), et la hauteur de chaque barre indique le nombre d'employés dans cette fourchette salariale.
    
    Échelles salariales courantes : les barres les plus hautes de l'histogramme se situent dans les échelles salariales [45 k€ - 49,99 k€] et [50 k€ - 54,99 k€]. Cela suggère que ces échelles salariales sont les plus courantes parmi nos employés, avec respectivement 23 et 22 employés.
    
    Répartition des salaires : l'histogramme montre que les salaires sont répartis sur une plage de valeurs relativement uniforme sans écarts ni regroupements significatifs.
    
    Asymétrie : l'histogramme semble être légèrement incliné vers la droite. Cela signifie qu'il y a relativement moins d'employés dans les échelles salariales inférieures ([20 k€ - 24,99 k€] à [40 k€ - 44,99 k€]) et plus d'employés dans les échelles salariales moyennes à supérieures ([45 k€ - 49,99 k€] à [65 k€ - 69.99 k€].
    """)

    st.markdown("")


    st.markdown("")


    st.markdown("- **Boîtes à moustaches** : Une boîte à moustache est un diagramme utilisé pour visualiser la répartition et l'asymétrie des **données quantitatives**. Elles sont particulièrement utiles pour détecter les valeurs aberrantes.")

    st.markdown("**Cas d’usage** des boîtes à moustaches : Elles peuvent être utilisés pour comparer différentes distributions d'une même **variable quantitative** (salaires, ancienneté, etc...)")

    st.markdown("")
    

    st.markdown("**🏀Application 11**")
    st.markdown("Disons que nous analysons les salaires des employés. Nous voulons voir comment les salaires sont répartis entre les différents services l'entreprise.")
    st.markdown("Nous pouvons créer un box plot pour visualiser la répartition des salaires pour chaque service. Le box plot nous montrera le salaire médian, l’écart interquartile et toutes les valeurs aberrantes.")


    import pandas as pd
    import numpy as np

# Create sample data
    np.random.seed(42)

# Simulate salaries for three departments: HR, Sales, and IT
    hr_salaries = np.random.normal(50000, 10000, 50)
    sales_salaries = np.random.normal(60000, 15000, 60)
    it_salaries = np.random.normal(65000, 12000, 45)

# Combine data into a DataFrame
    data = pd.DataFrame({
    'Service': ['RH'] * 50 + ['Ventes'] * 60 + ['IT'] * 45,
    'Salaire': np.concatenate([hr_salaries, sales_salaries, it_salaries])
    })

    import streamlit as st
    import plotly.express as px

# Create an interactive box plot using Plotly Express
    fig = px.box(data, x='Service', y='Salaire', title='Répartition des salaires au sein des services RH, Ventes & IT')
    fig.update_xaxes(title_text='Service')
    fig.update_yaxes(title_text='Salaire (k€)')

# Show the plot in Streamlit
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation des 3 box plot"):
        st.write("""
    La boîte représente l'écart interquartile (IQR) des salaires au sein de chaque service. Les bords inférieur (q1) et supérieur (q3) de la boîte correspondent respectivement aux 25e et 75e centiles. Cela nous indique où se situent 50% des salaires au sein de chaque service.
    
    La ligne à l'intérieur de la boîte représente le salaire médian pour chaque service. C'est la valeur salariale qui sépare les 50 % inférieurs des 50 % supérieurs.
    
    Les moustaches s'étendent de la boîte jusqu'aux valeurs minimales et maximales dans une plage de 1,5 fois l'IQR. Tous les points de données au-delà des moustaches sont considérés comme des valeurs aberrantes et sont affichés sous forme de points individuels.
    
    Comparaison des salaires : nous pouvons facilement comparer les répartitions salariales entre les 3 services RH, Ventes & IT. Par exemple, l'IT a le salaire médian le plus élevé (66.19 k€), suivi des Ventes (59.77 k€) et des RH (47.66 k€).
    
    Variabilité : La longueur de la boîte et des moustaches peuvent nous donner une idée de la variabilité salariale au sein de chaque service : une boîte ou des moustaches plus longues indiquent une plus grande variabilité.
    
    Valeurs aberrantes : le box plot du services Ventes nous aide à identifier des salaires individuels qui se situent bien en dehors de l'échelle salariale typique. Ils sont repésentés par 3 points individuels (20.70 k€, 30.19 k€ et 88.29 k€).
    """)


    st.markdown("")


    st.markdown("")


    st.markdown("- **Graphique linéaire** : Un graphique linéaire est un graphique qui affiche des **données quantitatives** au fil du temps. Il utilise des points connectés pour afficher les tendances et les modèles dans les données.")

    st.markdown("**Cas d’usage** des graphiques linéaires : Ils peuvent être utilisés pour suivre l'évolution des effectifs et de la masse salariale au fil du temps, pour visualiser l'absentéisme sur plusieurs mois, pour suivre les mesures de performance au fil du temps, etc...")


    st.markdown("")
    

    st.markdown("**🏀Application 12**")
    st.markdown("Supposons que nous disposions de données sur le total des salaires mensuels payés par l'entreprise au cours des trois dernières années (2020, 2021 et 2022). Nous pouvons utiliser un graphique linéaire comme outil de visualisation permettant de suivre l’évolution des salaires mensuels sur plusieurs années.") 
    st.markdown("Cette visualisation va nous permettre d'identifier les tendances, la saisonnalité et les valeurs aberrantes potentielles, permettant ainsi de prendre des décisions liées à la planification et à la budgétisation de la rémunération, fondées sur des données.") 
   

    import pandas as pd

# Create sample data for three years (in thousands of euros)
    data = pd.DataFrame({
    'Année': [2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020,
             2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021,
             2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022],
    'Mois': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre',
              'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre',
              'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
    'Salaire_Total': [120, 125, 122, 128, 162.5, 135, 138, 140, 145, 150, 152, 193.75,
                     160, 162, 165, 170, 215, 175, 178, 180, 182, 185, 190, 240,
                     195, 200, 202, 205, 260, 210, 212, 215, 220, 225, 230, 290]
    })

    import streamlit as st
    import plotly.express as px

# Create an interactive line chart using Plotly Express
    fig = px.line(data, x='Mois', y='Salaire_Total', color='Année', title='Suivi de la masse salariale sur 3 ans')
    fig.update_xaxes(title_text='Mois')
    fig.update_yaxes(title_text='Salaires totaux (en k€)')

# Show the plot in Streamlit
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation du graphique linéaire"):
        st.write("""
    Axe des x (Mois) : L'axe des X représente les mois de l'année, fournissant une dimension temporelle pour nos données.
    
    Axe des y (salaire total) : L'axe des y représente le total des salaires payés par l'entreprise en milliers d'euros pour chaque mois.
    
    Lignes par année : le graphique linéaire montre trois lignes, chacune d'une couleur différente, représentant les années 2020, 2021 et 2022. Ces lignes relient les points de données pour chaque mois, nous permettant d'observer les tendances au fil du temps.
    
    Tendances au fil du temps : nous pouvons voir comment les salaires mensuels totaux ont augmenté au cours des trois années. Ce qui peut être lié aux effectifs, à la structure de la masse salariale (effectifs par catégories de salariés), à l’ancienneté, à la législation, etc...
    
    Modèles saisonniers : On observons une saisonnalité car les salaires ont tendance à être bien plus élevés aux mois de mai et décembre, ce qui peut corrrespondre aux versements de primes (vacances, fin d'année, etc...)
    """)


    st.markdown("")


    st.markdown("")
    
    
    st.subheader("Données qualitatives et quantitatives")

    
    st.markdown("")


    st.markdown("")


    st.markdown("- **Nuage de points** : Un nuage de points est un type de visualisation de données qui montre la relation entre deux variables en plaçant des points de données sur les axes X et Y.")

    st.markdown("**Cas d’usage** des nuages de points : Ils peuvent être utilisés pour analyser la relation entre la satisfaction au travail et l'absentéisme, le niveau d'expérience et le salaire, les scores de performance des employés et les heures de formation suivies, etc...")


    st.markdown("")
    

    st.markdown("**🏀Application 13**")
    st.markdown("Nous souhaitons analyser la relation entre les scores de performance des collaborateurs et les heures de formation suivies. Nous pouvons utiliser un nuage de points avec droite ajustée et coefficient R².")


    import pandas as pd
    import numpy as np

# Create sample data for employee performance and training hours
    np.random.seed(42)

    employee_data = pd.DataFrame({
    'Score_de_Performance': np.random.randint(0, 100, 100),
    'Heures_de_formation_suivies': np.random.randint(0, 50, 100)
    })

    import streamlit as st
    import plotly.express as px

# Create an interactive scatter plot using Plotly Express
    fig = px.scatter(
    employee_data, x='Heures_de_formation_suivies', y='Score_de_Performance',
    title='Scatter Plot des Scores de performance vs. Heures de formation',
    trendline='ols'  # Add a linear regression line
    )
    fig.update_xaxes(title_text='Heures_de_formation_suivies')
    fig.update_yaxes(title_text='Score_de_Performance')

# Show the plot in Streamlit
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation du nuage de points"):
        st.write("""
    Axe des x : L'axe des x représente le nombre d'heures de formation suivies par chaque employé.
    
    Axe des y : L'axe des y représente les scores de performance des employés.
    
    Points de dispersion : chaque point de données sur le tracé représente un employé. La position du point indique leurs heures de formation et leur score de performance.
    
    Droite de régression linéaire : c'est la ligne la mieux adaptée qui décrit la relation entre les heures de formation et les scores de performance. Elle peut nous aider à identifier les tendances dans les données.
    
    Coefficient R² : Il quantifie dans quelle mesure la ligne de régression linéaire s'adapte aux données. Il mesure la force de la relation entre les deux variables.
    
    R² va de 0 à 1, où :

    1. R² = 0 : Le modèle n'explique aucune variabilité de la variable dépendante

    2. R² = 1 : Le modèle explique parfaitement la variabilité de la variable dépendante
 
    Dans notre cas, la valeur R² est de 0,018599, ce qui est assez faible. Cela suggère que seule une petite fraction (environ 1,86 %) de la variabilité des scores de performance peut être expliquée par le nombre d’heures de formation suivies.
    
    En d’autres termes, la relation linéaire entre les heures de formation et les scores de performance est faible. Cela indique que d'autres facteurs non inclus dans cette analyse peuvent avoir un impact plus important sur les scores de performance.
    """)
    

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
    redirect_button("https://cours-stats-rh.streamlit.app/Heatmap_en_bonus", "Suite : Heatmap")
    



        
        
        
        
        
        
