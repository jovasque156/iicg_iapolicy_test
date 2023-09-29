import streamlit as st
from PIL import Image
from markdownlit import mdlit
from streamlit_extras.stylable_container import stylable_container

st.markdown(
    """
    <style>
    .reportview-container {
        background: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

chart_1 = Image.open('assets/chart1.png')
chart_2 = Image.open('assets/chart2.png')
# Título de la página
st.title("Política sobre el Uso de Inteligencia Artificial en IICG")

# Introducción
mdlit("Consultores utilizando herramientas de Inteligencia Artifical (IAs) logran, en promedio, un 12,2% más de tareas, 25,1% más rápido, y con una calidad de un 40% más alta que sus pares que no usan IAs, encontró un **@(🔗)(estudio de investigadores)(https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)** de Harvard, UPenn, MIT, y Boston Consulting Group.")

cols = st.columns(spec=[.15,.7,.15])
with cols[1]:
    st.image(chart_1, 
             caption="Distribución (Density) de la calidad (Quality) del resultado de las tareas de los consultores. Los del grupo azul no usaron IAs, los del grupo verde y rojo usaron IAs. El grupo rojo recibió capacitación adicional sobre cómo usar la IA. Fuente: Dell'Acqua (2023)")


mdlit("Sabemos que las IAs son herramientas poderosas para mejorar el aprendizaje, la creatividad y la innovación. Pero también _**su uso implica desafíos y riesgos que debemos afrontar con criterio y responsabilidad**_. El mismo estudio mencionado arriba identificó que para ciertas tareas donde las IAs no tienen tan buen desempeño, consultores que usan IAs resultaban en trabajos de peores calidad de hasta ~25 puntos porcentuales comparados con sus pares sin usar IAs.")


cols = st.columns(spec=[.15,.7,.15])
with cols[1]:
    st.image(chart_2,
             caption="Desempeño promedio para la tarea 'fuera de la frontera', es decir, las IAs no completan suficientemente bien. Se informa el porcentaje de consultres de cada grupo que dieron una respuesta correcta en la tarea. Fuente: Dell'Acqua (2023)")


# st.write("Tenemos el agrado de presentar la política de uso de las herramientas de Inteligencia Artificial (de ahora en adelante IAs) dentro del aula, una iniciativa que busca fomentar el uso ético y responsable de las IAs en la formación académica.")


# st.write("Por ejemplo, un estudio realizado por investigadores de Harvard, UPenn, y MIT en Boston Consulting Group mostró que consultores usando IAs pueden producir resultados hasta un 40% más alto, ")


st.markdown("Por ello, hemos elaborado esta política con **[8 directrices](#directrices)** que orientan el uso de las IAs de manera justa, transparente y dentro del marco de libertad de cátedra.")


st.markdown("Extendemos la invitación a seguir esta política para integrar las IAs en la formación profesional de forma crítica y reflexiva. Confiamos de que esta política será un aporte para nuestra carrera y la comunidad que la conforma.")

# st.write("Esta política sobre el uso de las herramientas de Inteligencia Artificial (de ahora en adelante abreviadas como IAs) es una iniciativa que busca fomentar el uso ético y responsable de las IAs en los trabajos y proyectos dentro del aula.")
# st.write("La motivación de esta política es reconocer el potencial de las IAs para mejorar el aprendizaje, la creatividad y la innovación, pero también los desafíos y riesgos que implican su uso.")
# st.write("Por ello, la política establece 8 directrices para que estudiantes y docentes puedan usar las IAs de manera justa, transparente y dentro del marco de libertad de cátedra.")
# st.write("Esta política pretende generar conciencia sobre el impacto de las IAs, así como promover el desarrollo de competencias digitales propias de un IICG. La política en sí es una oportunidad para integrar las IAs en la formación de un IICG de forma crítica y reflexiva.")

# Declaración de política
st.header("Declaración de Política de Uso", divider='grey')
st.write("Como regla general:")

with stylable_container(
     key="container_with_border",
    css_styles="""
        {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px)
        }
        """,):
    mdlit("Ingeniería en Información y Control de Gestión **permite el uso de IAs** en trabajos y proyectos dentro del aula, siempre y cuando se _use de manera ética y responsable_. Esto incluye asegurarse de que las IAs se usen de manera _justa, transparente, responsable, y dentro del marco de libertad de cátedra de cada docente_.")                       
st.write("Con el objetivo de ayudar al cumplimiento de esta declaración, se han generado las siguientes directrices.")

# Directrices para el uso de IA
st.header("Directrices para el uso de IAs en clases", divider='grey', anchor='directrices')
st.write("Para garantizar que las IAs se usen de manera ética y responsable, hemos establecido las siguientes directrices:")

# Lista de directrices
st.write("1. Las IAs deben usarse para mejorar el aprendizaje y la investigación, no para reemplazar el trabajo y la toma de decisiones de cada persona.")
st.write("2. El uso de las IAs debe ser transparente y explicativo. Es decir, cada persona debe ser capaz de entender y explicar cómo usó las IAs y cómo llegó a los resultados finales con su uso.")
st.markdown("3. Cada persona que usa las IAs es responsable de tener un **[conocimiento básico de las IAs](#FAQ)** antes de utilizarla en sus trabajos, proyectos, y evaluaciones.")
st.write("4. Los y las estudiantes deben obtener la aprobación de su profesora o profesor antes de utilizar las IAs en las evaluaciones del curso.")
st.markdown("5. Cada trabajo y proyecto realizado con IAs debe tener una documentación clara de su uso en el mismo, incluyendo los datos utilizados, las IAs empleadas, los **[prompts](#FAQ)** aplicados, y los resultados obtenidos.")
st.write("6. Las IAs deben **[usarse de manera justa e imparcial](#FAQ)**, y no deben perpetuar o amplificar los sesgos existentes.")
st.write("7. Cada persona debe ser consciente de las limitaciones y posibles sesgos de las IAs, y debe tomar medidas para mitigarlos si es necesario.")
st.write("8. Cada persona debe respetar la privacidad y la seguridad de los datos que le entrega a las IAs utilizadas en sus trabajos y proyectos, y debe obtener el consentimiento de las personas propietarias de los datos si es necesario.")

# Definición de prompt
st.header("FAQ", divider='grey', anchor='FAQ')
with st.expander("# ¿Qué es un prompt?"):
    st.write("Un prompt es una instrucción o una pregunta que se proporciona a una IA para obtener una respuesta específica. Un prompt pueden ser simple o complejo, y pueden incluir información adicional para ayudar a la IA a generar una respuesta más cercano a lo esperado. Para obtener más información sobre como escribir un buen prompt, consulta este [enlace](https://www.evoacademy.cl/como-escribir-un-buen-prompt-en-chatgpt/).")
with st.expander("# ¿Dónde puedo aprender a usar IAs?"):
    st.write("Existen muchos recursos desde los cuales puedes aprender a usar la IA. Te recomendamos los siguientes")
    mdlit("- *@(📖)(Guía Práctica para usar IA)(https://www.oneusefulthing.org/p/the-practical-guide-to-using-ai-to)*, Ethan Mollick. Aunque está en inglés, puedes usar un traductor como @(🌎)(Google Translate)(https://translate.google.com/) para traducirla al español.")
    mdlit("- *@(📖)(Qué significa usar la IA como herramienta -de escritura-)(https://www.oneusefulthing.org/p/embracing-weirdness-what-it-means)*, Ethan Mollick. Este artículo está también en inglés, por tanto puedes utilizar Google Translate también.")
    st.write("Debes considerar que actualmente las IAs están cambiando día a día, y a una velocidad bastante alta. Por tanto, sugerimos fuertemente estar en constante revisión de los nuevos avances que van surgiendo")
    st.write("Adicionalmente, en IICG estaremos haciendo actividades, tales como charlas y talleres, en donde enseñaremos su uso correcto y cómo sacar provecho de las distintas herramientas. Puedes revisar en este [link]() las actividades que iremos haciendo")
with st.expander("# Quiero saber sobre las limitaciones y sesgos de las IAs, ¿Dónde puedo leer más al respecto?"):
    st.write("¡Felicitaciones por interesarte en este tema! Aunque este tema es bastante amplio y se viene estudiando desde hace un tiempo, sugerimos comenzar con los siguientes:")
    st.markdown("- 📖 _Fairness in Machine Learning_, Isabella Grabski. Este artículo publicado en 2020 habla de los sesgos en los modelos. En este [link](https://sitn-hms-harvard-edu.translate.goog/uncategorized/2020/fairness-machine-learning/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=wapp) podrás leer una versión traducida usando Google Translate.")
    st.markdown("- 🎦 _Algorithmic Bias and Fairness_, Crash Course. Este es un video que explica muy bien los sesgos y sus efectos. Lo podrás ver en este [link](https://www.youtube.com/watch?v=gV0_raKR2UQ&t=1s) Aunque está en inglés, puedes activar subtítulos de inglés a español.")
    st.markdown("- 🎦 _Coded Bias_, Shalini Kantayya. Este es un documental que discute sobre las limitaciones y los sesgos en las IAs. Puedes ver más en este link y si tienes acceso a Netflix, podrás ver el documental ahí.")
    st.markdown("Adicionalmente, en IICG estaremos haciendo actividades, tales como charlas y talleres, en donde enseñaremos su uso correcto y cómo sacar provecho de las distintas herramientas. Puedes revisar en este [link]() las actividades que iremos haciendo.")

st.header("Referencias", divider='grey', anchor='refs')
mdlit("- Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., ... & Lakhani, K. R. (2023). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality. _Harvard Business School Technology & Operations Mgt_. Unit Working Paper, (24-013).")
mdlit("- Mollick, E., & Mollick, L. (9 de Febrero, 2023). Why All Our Classes Suddenly Became AI Classes. _Harvard Business Publishing, Education_. https://hbsp.harvard.edu/inspiring-minds/why-all-our-classes-suddenly-became-ai-classes")