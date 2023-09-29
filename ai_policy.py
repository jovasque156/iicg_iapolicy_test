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
mdlit("El uso de herramientas de Inteligencia Artificial (IAs) puede marcar una gran diferencia en el desempeño de los consultores. Así lo demuestra un **@(🔗)(estudio de reconocidas universidades y consultoras)(https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)** (Harvard, UPenn, MIT, y Boston Consulting Group) que analizó el impacto del uso de IAs en la productividad, la velocidad y la calidad de los servicios de consultoría. El estudio encontró que los consultores que usan IAs logran, en promedio, **un 12,2% más de tareas, las realizan 25,1% más rápido, y con una calidad de un 40% más alta que los que no las usan**, tal como lo muestra la figura de abajo. Estos datos evidencian el enorme potencial de las IAs para su uso en el día a día.")

cols = st.columns(spec=[.15,.7,.15])
with cols[1]:
    st.image(chart_1, 
             caption="Distribución (Density) de la calidad (Quality) del resultado de las tareas de los consultores. Los del grupo azul no usaron IAs, los del grupo verde y rojo usaron IAs. El grupo rojo recibió capacitación adicional sobre cómo usar la IA. Fuente: Dell'Acqua (2023)")


mdlit("Las IAs son herramientas poderosas para mejorar el aprendizaje, la creatividad y la innovación. Pero **no son perfectas ni infalibles**. El mismo estudio mencionado arriba reveló que cuando se usan IAs para ciertas tareas donde tienen tan buen desempeño (identificadas técnicamente como _fuera de la frontera_), los consultores *pueden entregar trabajos de peores calidad de hasta ~25 puntos porcentuales comparados con sus pares sin usar IAs*, tal como lo revela la figura de más abajo. Esto nos muestra que las IAs **no pueden reemplazar el criterio y la responsabilidad de cada persona**. Al contrario, se deben usar con sabiduría y ética, aprovechando sus ventajas y evitando sus riesgos.")


cols = st.columns(spec=[.15,.7,.15])
with cols[1]:
    st.image(chart_2,
             caption="Porcentaje promedio de resultados correctos entregados por consultores para la tarea 'fuera de la frontera'. Fuente: Dell'Acqua (2023)")


st.markdown("Por ello, en la carrera de Ingeniería en Información y Control de Gestión hemos elaborado esta política con **[7 directrices](#directrices)** que orientan el uso de las IAs de manera segura, transparente y dentro del marco de libertad de cátedra.")


st.markdown("Extendemos la invitación a seguir esta política y así integrar las IAs en la formación y nuestro quehacer diario de forma crítica, reflexiva y responsable. Confiamos de que esta política será un aporte para la comunidad de IICG.")

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
            padding: calc(1em - 1px);
        }
        """,):
    st.markdown("Ingeniería en Información y Control de Gestión (IICG) **permite el uso de IAs** en el aula y ambientes de trabajo, siempre y cuando se _use de manera ética y responsable_. Esto incluye asegurarse de que las IAs sean usadas de manera _justa, transparente, responsable, y dentro del marco de libertad de cátedra_.", unsafe_allow_html=True)                       
st.write("Con el objetivo de ayudar al cumplimiento de esta declaración, hemos generado las siguientes directrices.")

# Directrices para el uso de IA
st.header("Directrices para el uso de IAs", divider='grey', anchor='directrices')
st.write("Para garantizar que las IAs se usen de manera ética y responsable, hemos establecido las siguientes directrices:")

# Lista de directrices
st.write("1. Cada persona debe usar las IAs para potenciar y complementar el aprendizaje y la investigación, sin reemplazar el trabajo y la autonomía de decisión.")
st.write("2. El uso de las IAs debe ser transparente y explicativo. Es decir, cada persona debe ser capaz de entender y explicar cómo usó las IAs y cómo llegó a los resultados finales.")
st.markdown("3. Quien usa las IAs es _responsable de tener un [conocimiento básico](#FAQ) de estas_ antes de utilizarla en sus trabajos, proyectos, y evaluaciones.")
st.write("4. Cada rofesor/a determinará el uso de las IAs para las evaluaciones de su asignatura.")
st.markdown("5. Los trabajos y proyectos realizados con IAs debe tener una documentación clara de su uso en el mismo, incluyendo los datos utilizados, las IAs empleadas, los **[prompts](#FAQ)** aplicados, y los resultados obtenidos.")
st.write("6. Quien use las IAs debe ser consciente de sus **[limitaciones y riesgos](#FAQ)**, y debe tomar medidas para mitigarlos si es necesario.")
st.write("7. Cada persona debe respetar la privacidad y la seguridad de los datos que le entrega a las IAs utilizadas en sus trabajos y proyectos, y debe obtener el consentimiento de las personas propietarias de los datos si es necesario.")

# Definición de prompt
st.header("FAQ", divider='grey', anchor='FAQ')
with st.expander("# ¿Qué es un prompt?"):
    st.write("Un prompt es una instrucción o una pregunta que se proporciona a una IA para obtener una respuesta específica. Un prompt pueden ser simple o complejo, y pueden incluir información adicional para ayudar a la IA a generar una respuesta más cercano a lo esperado. Para obtener más información sobre como escribir un buen prompt, consulta este [enlace](https://www.evoacademy.cl/como-escribir-un-buen-prompt-en-chatgpt/).")
with st.expander("# ¿Dónde puedo aprender a usar IAs?"):
    st.write("Existen muchos recursos desde los cuales puedes aprender a usar la IA. Te recomendamos los siguientes")
    mdlit("- *@(📖)(Guía Práctica para usar IA)(https://www.oneusefulthing.org/p/the-practical-guide-to-using-ai-to)*, Ethan Mollick. Aunque está en inglés, puedes usar un traductor como @(🌎)(Google Translate)(https://translate.google.com/) para traducirla al español.")
    mdlit("- *@(📖)(Qué significa usar la IA como herramienta -de escritura-)(https://www.oneusefulthing.org/p/embracing-weirdness-what-it-means)*, Ethan Mollick. Este artículo está también en inglés, por tanto puedes utilizar Google Translate también.")
    st.write("Debes considerar que actualmente las IAs están cambiando día a día a una velocidad alta. Por tanto, sugerimos estar en constante revisión de los nuevos avances que van surgiendo")
    st.write("Adicionalmente, como IICG estaremos haciendo actividades sobre este tema, tales como charlas y talleres, en donde enseñaremos su uso correcto y cómo sacar provecho de ellas. Puedes revisar este [enlace]() la lista de actividades.")
with st.expander("# Quiero saber sobre los riesgos y limitaciones de las IAs, ¿Dónde puedo leer más al respecto?"):
    st.write("¡Felicitaciones por el interés! Este tema es bastante amplio y se viene estudiando desde hace un tiempo. Las limitaciones son variadas, pero te sugerimos partir con estos recursos:")
    st.markdown("- 📖 _Fairness in Machine Learning_, Isabella Grabski. Este artículo publicado en 2020 habla de los sesgos en los modelos detrás de las IAs. En este [enlace](https://sitn-hms-harvard-edu.translate.goog/uncategorized/2020/fairness-machine-learning/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=wapp) podrás leer una versión traducida usando Google Translate.")
    st.markdown("- 📖 _Samsung prohíbe ChatGPT entre los empleados después de la filtración de código confidencial_, Forbes. Esta noticia habla sobre la filtración de código interno por parte de empleados de Samsung al usar ChatGPT. Revisa la nota traducida por Google Translate en este [link](https://www-forbes-com.translate.goog/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-chatbots-for-employees-after-sensitive-code-leak/?sh=7032bdda5df9&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en&_x_tr_pto=wapp&_x_tr_hist=true).")
    st.markdown("- 🎦 _Algorithmic Bias and Fairness_, Crash Course. Este es un video que explica muy bien los sesgos y sus efectos. Lo podrás ver en este [enlace](https://www.youtube.com/watch?v=gV0_raKR2UQ&t=1s) Aunque está en inglés, puedes activar subtítulos de inglés a español.")
    st.markdown("- 🎦 _Coded Bias_, Shalini Kantayya. Este es un documental que discute sobre las limitaciones y los sesgos en las IAs. Puedes ver más en este [enlace](https://www.codedbias.com/) y si tienes acceso a Netflix, podrás ver el documental [aquí](https://www.netflix.com/title/81328723).")
    st.markdown("Adicionalmente, como IICG estaremos haciendo actividades sobre este tema, tales como charlas y talleres, en donde enseñaremos su uso correcto y cómo sacar provecho de ellas. Puedes revisar este [enlace]() la lista de actividades.")

st.header("Referencias", divider='grey', anchor='refs')
mdlit("- Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., ... & Lakhani, K. R. (2023). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality. _Harvard Business School Technology & Operations Mgt_. Unit Working Paper, (24-013).")
mdlit("- Mollick, E., & Mollick, L. (9 de Febrero, 2023). Why All Our Classes Suddenly Became AI Classes. _Harvard Business Publishing, Education_. https://hbsp.harvard.edu/inspiring-minds/why-all-our-classes-suddenly-became-ai-classes")