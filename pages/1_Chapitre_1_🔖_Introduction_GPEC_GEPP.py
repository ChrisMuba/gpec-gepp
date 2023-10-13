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
        st.image('GIF/GIF_Chap1B.gif')

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


    
    
    st.markdown("Pour y arriver ils peuvent : ") 
                
    st.markdown("- **Créer des indicateurs** : concernant par exemple le **suivi des effectifs**, la **pyramide des âges**, la **pyramide des anciennetés**, le **suivi de la masse salariale**, le **suivi du turn-over**, le **suivi de l'absentéisme**, la **qualité du recrutement**, le **climat interne**, etc...") 

    st.markdown("*📌Les possibilités de création d'indicateurs RH sont nombreuses et dépendent des objectifs suivis par l'entreprise et des données à disposition.*")

    st.markdown("")

    st.markdown("- **Créer des tableaux de bord** : après avoir défini les indicateurs RH à suivre et collecté les données appropriées, nous pouvons créer un tableau de bord automatisé qui rassemblera et facilitera le suivi en temps réel de nos indicateurs.")

    st.markdown("📌*Les outils pour créer des tableaux de bords RH sont nombreux : parmi les solutions « presse-bouton » mais peu flexibles certaines bien rodées sont Power BI, Tableau, Qlik ou Looker Studio ; en revanche si on sait écrire du code, les possibilités sont presque sans limites avec Streamlit (framework Python🐍), Flexdashboard (framework R), Shiny (R / Python🐍), etc... .*")


    st.markdown("")


    st.markdown("Ci-dessous un :blue[exemple de **tableau de bord RH**] à 4 onglets :") 
    
    st.markdown("- Suivi de la masse salariale") 
    st.markdown("- Pyramide des âges") 
    st.markdown("- Répartition H/F")
    st.markdown("- Salaire moyen H/F")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objs as go
    import plotly.express as px
   

# Line Plot
    # Monthly payroll data (in thousands of dollars)
    forecast_months_2023 = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    réalisé_months_2023 = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août']

    forecast_2023 = [1154300, 1200010, 1235205, 1305008, 1778120, 1263150, 1208180, 1240000, 1275002, 1299250, 2356280, 1251300]
    réalisé_2023 = [1152003, 1185350, 1113880, 1205008, 1677420, 1121245, 1148000, 1165000]

# Create a dataframe for plotting
    df = pd.DataFrame({'mois': forecast_months_2023 + réalisé_months_2023,
                       'forecast 2023 (prévision)': forecast_2023 + [None] * len(réalisé_months_2023),
                       'réalisé 2023': [None] * len(forecast_months_2023) + réalisé_2023})

# Create an interactive line plot
    fig_1 = px.line(df, x='mois', y=['forecast 2023 (prévision)', 'réalisé 2023'],
                    labels={'value': 'masse salariale brute (millions €)'},
                    title='suivi de la masse salariale (prévision 2023 vs. réalisé 2023)')

# Customize line colors
    fig_1.update_traces(line_color='red', selector=dict(name='forecast 2023 (prévision)'))
    fig_1.update_traces(line_color='blue', selector=dict(name='réalisé 2023'))

# Display the line plot
  #st.plotly_chart(fig_1)
    

    st.markdown("")


# Age Pyramid
# Define age intervals
    age_intervals = ['[ < 25]', '[25 - 29]', '[30 - 34]', '[35 - 39]', '[40 - 44]', '[45 - 49]', '[50 - 54]', '[55 - 59]', '[60 et +]']

# Corresponding y values for the intervals
    y = list(range(len(age_intervals)))

    women_bins = np.array([-1686, -3868, -3463, -2346, -2074, -3037, -3495, -4194, -228])
    men_bins = np.array([887, 2013, 2323, 1842, 1645, 2270, 3115, 3891, 493])

    layout = go.Layout(
    title='Pyramide des âges en pelote de laine',
    yaxis=go.layout.YAxis(title='Âge', tickvals=y, ticktext=age_intervals),
    xaxis=go.layout.XAxis(
        range=[-5000, 5000],
        tickvals=[-4000, -2000, 0, 2000, 4000],
        ticktext=[4000, 2000, 0, 2000, 4000],
        title='Effectif'
    ),
    barmode='overlay',
    bargap=0.1
)

    data = [
    go.Bar(
        y=y,
        x=men_bins,
        orientation='h',
        name='👦🏿 Homme',
        hoverinfo='x',
        marker=dict(color='#1f77b4')
    ),
    go.Bar(
        y=y,
        x=women_bins,
        orientation='h',
        name='👩‍🦰 Femme',
        text=-1 * women_bins.astype('int'),
        hoverinfo='text',
        marker=dict(color='#e377c2')
    )
]

    fig_2 = go.Figure(data=data, layout=layout)
    
    #st.plotly_chart(fig_2)


    st.markdown("")
    

# Pie Chart
    # Répartition 👦🏿/👩‍🦰

    data = ["femme", "homme", "femme", "homme", "homme"]
    colors = ['#e377c2', '#1f77b4']

    def fig_3(data, colors, title):
        gender_counts = {gender: data.count(gender) for gender in set(data)}
        labels = list(gender_counts.keys())
        values = list(gender_counts.values())

        fig_3 = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
        fig_3.update_layout(title=title)
        return fig_3

    fig_3 = fig_3(data, colors, "Répartition H/F")
    #st.plotly_chart(fig_3)


# Bar Chart
    # Sample dataset
    data = {
    'Employee ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Genre': ['Homme👦🏾', 'Femme👧', 'Homme👦🏾', 'Femme👧', 'Homme👦🏾', 'Homme👦🏾', 'Femme👧', 'Femme👧', 'Homme👦🏾', 'Femme👧'],
    'Salaire €': [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000]
    }

    df = pd.DataFrame(data)

    # Average salary by gender
    #st.markdown('**fig.2: Salaire moyen selon le genre**')
    avg_salary = df.groupby('Genre')['Salaire €'].mean().reset_index()

    fig_4 = px.bar(avg_salary, x='Genre', y='Salaire €', title='Comparaison du salaire moyen entre H/F', color='Genre',
                     color_discrete_map={'Homme👦🏾': '#1f77b4', 'Femme👧': '#e377c2'})
    #st.plotly_chart(fig_4)

    st.markdown("")


    st.markdown("")
    
    
    # Create the tabs
    tabs = st.tabs(["Suivi de la masse salariale", "Pyramide des âges", "Répartition H/F", "Salaire moyen H/F"])

# Tab 1 - Line Chart
    with tabs[0]:
        #st.write("## Line Chart")
        st.plotly_chart(fig_1)

# Tab 2 - Histogram
    with tabs[1]:
        #st.write("## Histogram")
        st.plotly_chart(fig_2)

# Tab 3 - Pie Chart
    with tabs[2]:
        #st.write("## Pie Chart")
        st.plotly_chart(fig_3)

# Tab 4 - Bar Chart
    with tabs[3]:
        #st.write("## Bar Chart")
        st.plotly_chart(fig_4)

    
    st.markdown("")


    st.markdown("")
    

    st.markdown("- **Remplir les obligations légales** : notamment construire le **bilan social**, préparer et mettre à dsposition les **données necessaires à la négociation annuelle obligatoire** (NAO) ; ") 
    
    st.markdown("- Calculer l'**index égalité** H/F ; effectuer la **déclaration annuelle obligatoire d’emploi des travailleurs handicapés** (DOETH), etc...") 
    
    st.markdown("🚀**Tous ces éléments sont basés sur la collecte et l'analyse de données sociales, et requièrent donc une excellente compréhension des concepts et méthodes statistiques**.🚀")


    st.markdown("")
    
    
    st.markdown("Les statistiques appliquées aux RH permettent aussi la **réalisation d'études ponctuelles**, sur des sujets précis, pouvant conduire à la mise en place de diverses actions correctives.")
    

    st.markdown("")


    st.markdown("")


    st.markdown("**🏀Application 1**")

    st.markdown("Nous menons une étude dans laquelle nous souhaitons comparer le nombre de jours d'absence au sein de différents services sur une période donnée ; et ainsi déceler d'éventuels problèmes de climat social au sein de certaines équipes.")
    
    st.markdown("Ci-dessous un échantillon données : ")
    

    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    from statsmodels.stats.multicomp import pairwise_tukeyhsd

     # Sample dataset
    data = pd.read_csv('csv_files/employee_absence_data.csv')

    # Remove leading/trailing spaces from column names
    data.columns = data.columns.str.strip()

    st.markdown("**Tableau de suivi des absences des employés**")

# Display the data
    st.write(data)

    st.markdown("")

    st.markdown("Nous visualisons la répartition des jours d'absence à l'aide de Box Plot, qui montrent des variations d'absence selon les différents services.")

    
    fig = px.box(data, x='Department', y='Days_of_Absence', title='Box Plot : Jours d\'absence par service')
    st.plotly_chart(fig)


    # Explanation
    with st.expander("🔮Interpretation"):
        st.write("""
        **Tableau ANOVA** : La statistique F (F) est d'environ 4.8257 et la p-value (PR(>F)) associée est de 0.011, ce qui est inférieur au seuil typique de significativité de *0.05*.
        **Cela indique qu’il existe une différence statistiquement significative dans les jours d’absence entre au moins certains services**.

        ⚠️ Dans notre cas il faut compléter l'analyse à l'aide d'un **test HSD de Tukey** pour identifier quelles paires de services spécifiques ont des jours d'absence moyens significativement différents,
        ce qui permettra d'orientier de façon efficiente la mise en place d'actions correctives.

        """)

    st.markdown("")

    anova_model = ols('Days_of_Absence ~ Department', data=data).fit()
    anova_table = sm.stats.anova_lm(anova_model, typ=2)

    st.markdown("Nous effectuons un test d'ANOVA unidirectionnel pour vérifier s'il existe des différences significatives dans les jours d'absence entre les départements. Si la valeur p est inférieure à 0.05, on peut conclure qu’au moins un service est significativement différent des autres.")
    
    st.write("Table d\'ANOVA:")
    st.write(anova_table)

    st.markdown("")

    st.markdown("")

    st.markdown("📌 *Les possibilités de sujets d'études statistiques sont très nombreuses en RH et dépendent des problématiques et objectifs propres à chaque entreprises* :")

    st.markdown("1. :blue[**Engagement des employés** :] Mesurer et analyser les niveaux d'engagement des employés peut aider les entreprises à identifier les domaines dans lesquels elles peuvent **améliorer la satisfaction et la productivité des employés**.")

    st.markdown("2. :blue[**Acquisition de talents** :] Aider les entreprises à comprendre leur processus d'embauche et à identifier les domaines dans lesquels il peut être amélioré. Cela peut inclure des études sur l'efficacité des différents canaux de recrutement, le temps qu'il faut pour embaucher pour différents postes, le coût de l'embauche de nouveaux employés, etc...")
                
    st.markdown("3. :blue[**Fidélisation des employés** :] Aider les entreprises à comprendre pourquoi les employés quittent leur emploi et à **identifier des moyens pour réduire le turnover**. Cela peut inclure des études sur les différentes raisons de départ, **le coût du turnover, l'impact du turnover sur les résultats financiers de l'entreprise**, etc...")

    st.markdown("4. :blue[**Rémunération et avantages sociaux** :] S'assurer que les entreprises offrent des packages de rémunération et avantages sociaux compétitifs. Cela peut inclure des études sur les salaires et les avantages sociaux du marché, la satisfaction des employés à l'égard de la rémunération et des avantages sociaux, et **l'impact de la rémunération et des avantages sociaux sur la fidélisation des employés**, etc...")

    st.markdown("5. :blue[**Formation et développement des compétences** :] Aider les entreprises à évaluer l'efficacité de leurs programmes de formation et de développement des compétences. Cela peut inclure des études sur la satisfaction des employés à l'égard des programmes de formation et de développement des compétences, **l'impact de ces programmes sur les performances des employés et le retour sur investissement des programmes de formation et de développement**.")

    st.markdown("6. :blue[**Commentaires et communication des employés** :] Examiner l'efficacité des canaux de rétroaction et de communication au sein de l'entreprise et identifier les opportunités d'amélioration en favorisant un environnement de travail transparent et collaboratif.")

    st.markdown("7. :blue[etc...]")

    st.markdown("")

    st.markdown("Ce ne sont là que quelques exemples d’études RH qui peuvent être menées en entreprise. Les études spécifiques les plus pertinentes dépendront des besoins de l’entreprise.")

    st.markdown("")

    #url = "https://cours-stats-rh.streamlit.app/Quiz_1_-_Introduction_aux_Statistiques📉"
    #st.write("Acceder au quiz du chapitre 1 [ici](%s)" % url)

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
    redirect_button("https://cours-stats-rh.streamlit.app/Quiz_1_-_Introduction_aux_Statistiques📉","Quiz du chapitre 1")


                
    



    
   




    



    



