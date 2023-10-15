


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Chapitre 6")

st.sidebar.markdown("# Chapitre 6")

st.title("Mise en œuvre et gestion du changement")

st.markdown("La mise en œuvre d'un plan stratégique de main-d'œuvre est une phase critique dans le processus d'alignement de la main-d'œuvre de votre organisation sur ses objectifs stratégiques. La réussite de la mise en œuvre dépend d’une gestion efficace du changement, car elle implique souvent des changements organisationnels importants.") 

st.markdown("")

if st.button("Cliquez pour acceder au Chap.6 - **A/ Déployer le plan de main d'œuvre**"):
    
    st.subheader("📗Chap.6-A/ Déployer le plan de main d'œuvre📘")
    
    
    st.markdown("- **Plans d'action détaillés** : commencez par traduire la planification stratégique de la main d'œuvre en plans d'action détaillés qui précisent ce qui doit être fait, quand, par qui et avec quelles ressources. Ces plans d’action doivent s’aligner sur les objectifs stratégiques plus larges.") 
    
    st.markdown("- **Attribution des responsabilités** : attribuez clairement les responsabilités aux membres de l'équipe ou aux services pour garantir que chacun comprend son rôle dans l'exécution du plan.")

    st.markdown("- **Échéanciers et jalons** : Élaborez des échéanciers et des jalons pour chaque plan d'action, en vous assurant qu'ils sont réalistes et réalisables.")

    st.markdown("- **Planification de la succession** : identifier et développer les talents internes pour des rôles clés est un moyen proactif de prévoir les besoins en talents. En évaluant l’état de préparation de vos employés à accéder à des postes à responsabilités, vous pouvez réduire le recours au recrutement externe.")
    
    st.markdown("- **Indicateurs de performance** : définissez des indicateurs clés de performance (KPI) et des critères de réussite qui vous aideront à mesurer les progrès et l'impact du plan de main-d'œuvre.")

    st.markdown("- **Allocation des ressources** : allouer les ressources nécessaires, y compris le budget, la main-d'œuvre et la technologie, pour soutenir l'exécution du plan.")
                
    st.markdown("")
    

        
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/take_notes.gif')

if st.button("Continuer vers la suite du Chap.2 - **B/ Planification de scénarios et modélisation de la main-d'œuvre**"):
    
    st.subheader("📗Chap.6-B/ Communiquer le plan aux parties prenantes📘")
    
    st.markdown("") 
    
    st.markdown("- **Identification des parties prenantes** : identifiez toutes les parties prenantes impliquées ou affectées par la planification stratégique. Cela inclut les dirigeants, les chefs de service, les équipes RH et les employés.")

    st.markdown("- **Messages personnalisés** : éadaptez votre communication pour répondre aux préoccupations et aux intérêts spécifiques des différentes parties prenantes. Utilisez un langage qui trouve un écho auprès de chaque groupe.")

    st.markdown("- **Transparence** : soyez ouvert et transparent sur les objectifs de la planification stratégique de la main-d'œuvre, son impact attendu et les avantages qu'il apportera à l'organisation.")

    st.markdown("- **Mécanismes de rétroaction** : établir des mécanismes de rétroaction qui permettent aux parties prenantes de partager leurs préoccupations, leurs questions et leurs suggestions. Il est essentiel de répondre aux préoccupations de manière proactive pour obtenir l’adhésion.")

    st.markdown("- **Mises à jour continues** : Tenez les parties prenantes informées des progrès de la planification stratégique et de tout ajustement apporté au plan en fonction de l'évolution des circonstances.")

    st.markdown("- ** Formation et soutien** : Fournir une formation et un soutien pour garantir que les parties prenantes comprennent leur rôle dans la mise en œuvre du plan.")
                

    st.markdown("")


if st.button("Continuer vers la suite du Chap.2 - **C/ Identifier les rôles et compétences critiques**"):
    
    st.subheader("📗Chap.6-C/ Identifier rôles et compétences critiques📘")
    
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

    
    



        
        
        
        
        
        
