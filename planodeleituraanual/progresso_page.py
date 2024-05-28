from streamlit.delta_generator import DeltaGenerator


def index(tab: DeltaGenerator):

    tab.write('## Seu Progresso')
