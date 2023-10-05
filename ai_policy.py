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
st.title("Política sobre el Uso de Herramientas de Inteligencia Artificial en IICG")

# Introducción
mdlit("El uso de herramientas de Inteligencia Artificial (IA) puede marcar una gran diferencia en el desempeño de una persona. Así lo demuestra un **@(🔗)(estudio de reconocidas universidades y consultoras)(https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)** (Harvard, UPenn, MIT, y Boston Consulting Group) que analizó el impacto del uso de herramientas de IA en la productividad, la velocidad y la calidad de los servicios de consultoría. El estudio encontró que los consultores que utilizan herramientas de IA logran, en promedio, **un 12,2% más de tareas, 25,1% más rápido y con una calidad de un 40% más alta que los que no las usan**, tal como lo muestra la figura de abajo. Estos datos evidencian el enorme potencial de las herramientas de IA para su uso en el día a día.")

cols = st.columns(spec=[.15,.7,.15])
with cols[1]:
    st.image(chart_1, 
             caption="Distribución (Density) de la calidad (Quality) del resultado de las tareas de los consultores. En el grupo azul no se utilizaron herramientas de IA, mientras que en los grupos verde y rojo sí se hicieron uso de ellas. El grupo rojo recibió capacitación adicional sobre cómo usar estas herramientas. Fuente: Dell'Acqua (2023)")


mdlit("Así como en consultaría, las herramientas de IA pueden ser un elemento crucial para mejorar el aprendizaje, la creatividad y la innovación. **Pero no son perfectas ni infalibles**. El mismo estudio mencionado arriba (@(📖)(descargar aquí)(https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321)) revela que cuando se usan herramientas de IA en tareas donde esta tiende a equivocarse (identificadas como tareas ubicadas _fuera de la frontera de una IA_), los consultores *entregan trabajos de peores calidad comparados con sus pares sin usar herramientas de IA*. La diferencia podía ser de hasta ~25 puntos porcentuales, tal como lo revela la figura de más abajo.  Esto nos muestra que las herramientas de IA **no pueden reemplazar el criterio y la responsabilidad de cada persona**. Al contrario, se deben usar con sabiduría y ética, aprovechando sus ventajas y evitando sus riesgos.")


cols = st.columns(spec=[.15,.7,.15])
with cols[1]:
    st.image(chart_2,
             caption="Porcentaje promedio de resultados correctos entregados por consultores para una tarea 'fuera de la frontera'. Fuente: Dell'Acqua (2023)")


st.markdown("Por ello, en la carrera de Ingeniería en Información y Control de Gestión hemos elaborado esta política con **[7 directrices](#directrices)** que orientan el uso ético y responsable de las herramientas de IA.")


st.markdown("Extendemos la invitación a seguir esta política y así integrar las herramientas de IA en la formación y nuestro quehacer diario de forma crítica y reflexiva. Confiamos de que esta política será un aporte para nuestra comunidad.")

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
    st.markdown("Ingeniería en Información y Control de Gestión (IICG) **permite el uso de herramientas de IA** en el aula y ambientes de trabajo, siempre y cuando se _use de manera ética y responsable_. Esto incluye asegurarse   \nde que sean usadas de manera _justa, transparente, responsable, y dentro del marco de libertad de   \n cátedra_.", unsafe_allow_html=True)                       

# Directrices para el uso de IA
st.header("Directrices para el uso de herramientas de IA", divider='grey', anchor='directrices')
st.write("Para garantizar que las distintas IA se usen de manera ética y responsable, hemos establecido las siguientes directrices:")

# Lista de directrices
st.write("1. Cada persona, al usar las aplicaciones de IA, lo debe hacer con foco en potenciar y complementar el aprendizaje y la investigación, sin reemplazar el trabajo y la autonomía de decisión.")
st.write("2. El uso de las herramientas de IA debe ser transparente y explicativo. Es decir, cada persona debe ser capaz de entender y explicar cómo las usó y cómo llegó a los resultados finales.")
st.markdown("3. Quien use las distintas IA es responsable de tener un **[conocimiento básico](#FAQ)** de estas antes de emplearlas en sus trabajos, proyectos, y evaluaciones.")
st.write("4. Cada profesor/a determinará el uso de herramientas de IA en las evaluaciones de su asignatura.")
st.markdown("5. Los trabajos y proyectos realizados con aplicaciones de IA deben tener una documentación clara de su uso en los mismos, incluyendo los datos utilizados, las herramientas de IA empleadas, los **[prompts](#FAQ)** aplicados, y los resultados obtenidos.")
st.write("6. Quien use las heramientas de IA debe ser consciente de sus **[limitaciones y riesgos](#FAQ)**, tomando medidas para mitigarlos si es necesario.")
st.write("7. Cada persona debe respetar la privacidad y la seguridad de los datos que le entrega a la aplicaciones de IA, y debe obtener el consentimiento de las personas propietarias de los datos si es necesario.")

# Definición de prompt
st.header("FAQ", divider='grey', anchor='FAQ')
with st.expander("# ¿Dónde puedo aprender sobre como usar las distintas IA?"):
    st.write("Existen muchos recursos desde los cuales puedes aprender a usar las herramientas de IA. Te recomendamos los siguientes:")
    mdlit("- *@(📖)(Guía Práctica para usar herramientas de IA)(https://www.oneusefulthing.org/p/the-practical-guide-to-using-ai-to)*, Ethan Mollick. Aunque está en inglés, puedes usar un traductor como @(🌎)(Google Translate)(https://translate.google.com/) para traducirla al español.")
    mdlit("- *@(📖)(Qué significa usar la IA como herramienta -de escritura-)(https://www.oneusefulthing.org/p/embracing-weirdness-what-it-means)*, Ethan Mollick. Este artículo está también en inglés, así que puedes utilizar @(🌎)(Google Translate)(https://translate.google.com/) para traducir la página web.")
    st.write("")
    st.write("Las herramientas de IA están en constante evolución y cada día surgen nuevos avances. Por lo tanto, te recomendamos que estés al día con las últimas novedades y tendencias.")
    st.write("Adicionalmente, como IICG estaremos haciendo actividades, tales como charlas y talleres, en donde enseñaremos el uso correcto de herramientas IA y cómo sacar provecho de ellas. Puedes revisar en este [enlace]() la lista de actividades.")
with st.expander("# ¿Qué es un prompt?"):
    st.write("Un prompt es una instrucción o una pregunta que se proporciona a una IA para obtener una respuesta específica. Un prompt pueden ser simple o complejo, y pueden incluir información adicional para ayudar a la aplicación de IA a generar una respuesta más cercano a lo esperado. Para obtener más información sobre como escribir un buen prompt, consulta este [enlace](https://www.evoacademy.cl/como-escribir-un-buen-prompt-en-chatgpt/).")
with st.expander("# ¿Dónde puedo aprender sobre los riesgos y limitaciones de las aplicaciones de IA?"):
    st.write("¡Felicitaciones por el interés! Este tema es bastante amplio y se viene estudiando desde hace un tiempo. Las limitaciones y riesgos son variados, pero te sugerimos partir con estos recursos:")
    st.markdown("- 📖 _Fairness in Machine Learning_, Isabella Grabski. Este artículo publicado en 2020 habla de los sesgos en los modelos detrás de las aplicaciones de IA. En este [enlace](https://sitn-hms-harvard-edu.translate.goog/uncategorized/2020/fairness-machine-learning/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=wapp) podrás leer una versión traducida usando Google Translate.")
    st.markdown("- 📖 _Samsung prohíbe ChatGPT entre los empleados después de la filtración de código confidencial_, Forbes. Esta noticia habla sobre la filtración de código interno por parte de empleados de Samsung al usar ChatGPT. Revisa la nota traducida por Google Translate en este [link](https://www-forbes-com.translate.goog/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-chatbots-for-employees-after-sensitive-code-leak/?sh=7032bdda5df9&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en&_x_tr_pto=wapp&_x_tr_hist=true).")
    st.markdown("- 🎦 _Algorithmic Bias and Fairness_, Crash Course. Este es un video que explica muy bien los sesgos y sus efectos en las herramientas de IA. Lo podrás ver en este [enlace](https://www.youtube.com/watch?v=gV0_raKR2UQ&t=1s). El video está en inglés, pero tiene habilitado subtítulos en español.")
    st.markdown("- 🎦 _Coded Bias_, Shalini Kantayya. Este es un documental que discute sobre las limitaciones y los sesgos en la herramientas de IA. Puedes ver más en este [enlace](https://www.codedbias.com/) y si tienes acceso a Netflix, podrás ver el documental [aquí](https://www.netflix.com/title/81328723).")
    st.markdown("- 📖 _¿Qué son las alucinaciones de la aplicaciones de IA?_, IBM. En [este](https://www-ibm-com.translate.goog/topics/ai-hallucinations?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en&_x_tr_pto=wapp) artículo la empresa IBM entrega una descripción de este fenómeno, sus implicancias y cómo podemos prevenirlas.")
    st.write("")
    st.markdown("Adicionalmente, como IICG estaremos haciendo actividades tales como charlas y talleres, en donde enseñaremos las limitaciones, riesgos y cómo mitigarlos. Puedes revisar este [enlace]() la lista de actividades.")
with st.expander("# ¿Dónde aprender más sobre la explicabilidad de las herramientas IA?"):
    st.write("Las herramientas IA son consideradas _black box_, por la complejidad y profundidad de los modelos de _machine learning_ que están detrás de cada una de ellas. Dado esto, en el área es considerado un desafío importante aumentar la explicabilidad. Para adentrarte en el tema, te sugerimos los siguientes recursos académicos:")
    mdlit("- *@(📖)(Interpretabilidad y Explicabilidad - Un mini recorrido)(https://arxiv.org/abs/2012.01805)*, Marcinkevičs & Vogt. Este es un artículo de investigación que revisa el diseño de la explicabilidad e interpretabilidad de los modelos.")
    mdlit("- *@(📖)(IA Explicable: una revisión de los métodos de interpretabilidad del aprendizaje automático)(https://www.mdpi.com/1099-4300/23/1/18)*, Linardatos, Papastefanopoulos, y Kotsiantis. Esta es otro artículo de revisión literaria que aborda el XAI: Explainable Artificial Intelligence.")
    st.write("")
    st.markdown("Adicionalmente, como IICG estaremos haciendo actividades tales como charlas y talleres, en donde enseñaremos las limitaciones, riesgos y cómo mitigarlos. Puedes revisar este [enlace]() la lista de actividades.")
st.header("Referencias", divider='grey', anchor='refs')
mdlit("- Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., ... & Lakhani, K. R. (2023). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality. _Harvard Business School Technology & Operations Mgt_. Unit Working Paper, (24-013).")
mdlit("- Mollick, E., & Mollick, L. (9 de Febrero, 2023). Why All Our Classes Suddenly Became AI Classes. _Harvard Business Publishing, Education_. https://hbsp.harvard.edu/inspiring-minds/why-all-our-classes-suddenly-became-ai-classes")