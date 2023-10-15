


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

if st.button("Continuer vers la suite du Chap.6 - **B/ Planification de scénarios et modélisation de la main-d'œuvre**"):
    
    st.subheader("📗Chap.6-B/ Communiquer avec les parties prenantes📘")
    
    st.markdown("") 
    
    st.markdown("- **Identification des parties prenantes** : identifiez toutes les parties prenantes impliquées ou affectées par la planification stratégique. Cela inclut les dirigeants, les chefs de service, les équipes RH et les employés.")

    st.markdown("- **Messages personnalisés** : éadaptez votre communication pour répondre aux préoccupations et aux intérêts spécifiques des différentes parties prenantes. Utilisez un langage qui trouve un écho auprès de chaque groupe.")

    st.markdown("- **Transparence** : soyez ouvert et transparent sur les objectifs de la planification stratégique de la main-d'œuvre, son impact attendu et les avantages qu'il apportera à l'organisation.")

    st.markdown("- **Mécanismes de rétroaction** : établir des mécanismes de rétroaction qui permettent aux parties prenantes de partager leurs préoccupations, leurs questions et leurs suggestions. Il est essentiel de répondre aux préoccupations de manière proactive pour obtenir l’adhésion.")

    st.markdown("- **Mises à jour continues** : Tenez les parties prenantes informées des progrès de la planification stratégique et de tout ajustement apporté au plan en fonction de l'évolution des circonstances.")

    st.markdown("- ** Formation et soutien** : Fournir une formation et un soutien pour garantir que les parties prenantes comprennent leur rôle dans la mise en œuvre du plan.")
                

    st.markdown("")


if st.button("Continuer vers la suite du Chap.6 - **C/ Gérer le changement organisationnel**"):
    
    st.subheader("📗Chap.6-C/ Gérer le changement organisationnel📘")
    
    
    st.markdown("- **Ambassadeurs du changement** : nommez des ambassadeurs du changement au sein de l'organisation qui peuvent aider à guider et à soutenir leurs pairs tout au long du processus.")

    st.markdown("- **Formation et développement** : Fournir les programmes de formation et de développement nécessaires pour doter les employés des compétences et des connaissances requises pour l'évolution de leurs rôles.")

    st.markdown("- **Alignement culturel** : veiller à ce que la culture organisationnelle s'aligne sur les objectifs et les valeurs de la planification stratégique. Cela peut nécessiter des ajustements culturels pour accueillir le changement et l’innovation.")

    st.markdown("- **Canaux de communication** : maintenir des canaux de communication ouverts pour répondre aux préoccupations et rassurer en période de changement.")

    st.markdown("- **Boucles de rétroaction** : mettez en œuvre des boucles de rétroaction qui permettent aux employés d'exprimer leurs pensées, leurs préoccupations et leurs suggestions, et de répondre activement à leurs commentaires.")

    st.markdown("- **Suivi et évaluation** : surveiller en permanence la mise en œuvre de la planification stratégique et évaluer son efficacité. Apportez les ajustements nécessaires pour garantir que le plan reste sur la bonne voie.

    st.markdown("- **Célébrer le succès** : Reconnaître et célébrer les étapes et les succès obtenus grâce à la planification stratégique. Cela peut motiver les employés et susciter l’enthousiasme pour le plan.

    st.markdown("")

    st.markdown("Une mise en œuvre efficace et une gestion du changement sont essentielles au succès de votre plan stratégique de main-d’œuvre. En déployant le plan avec des plans d'action clairs, en impliquant les parties prenantes et en gérant le changement organisationnel de manière proactive, vous pouvez vous assurer que votre organisation s'adapte efficacement à la nouvelle stratégie de main-d'œuvre et s'aligne sur ses objectifs stratégiques.")

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
    redirect_button("https://gpec-gepp.streamlit.app/Quiz_3_-_Pr%C3%A9voir_les_besoins_en_talents📉","Quiz du chapitre 3")

    
    



        
        
        
        
        
        
