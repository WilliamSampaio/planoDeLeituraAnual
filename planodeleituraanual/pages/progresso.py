import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def index(tab: DeltaGenerator):

    tab.write('## Seu Progresso')
    tab.caption('Acompanhe seu progresso no plano de leitura.')

    prog_df = st.session_state.biblia_df

    prog_df['percentual'] = [
        prog_df['capitulos_lidos'][i] / prog_df['capitulos'][i]
        for i in range(len(prog_df))
    ]

    tab.progress(
        prog_df['capitulos_lidos'].sum() / prog_df['capitulos'].sum(),
        'Progresso geral',
    )

    sec1 = tab.expander('Progresso por Livro', True)

    columns_size = [1, 0.3, 0.4, 0.3, 0.7, 0.1]

    header = sec1.columns(columns_size)

    header[0].write('#### Livro')
    header[1].write('#### Capítulos')
    header[2].write('#### Capítulos Lidos')
    header[3].write('#### Percentual')
    header[4].write('#### Progresso')

    for i in range(len(prog_df)):

        linha = sec1.columns(columns_size)
        linha[0].markdown('##### {}'.format(prog_df['livro'][i]))
        linha[1].markdown('##### {}'.format(prog_df['capitulos'][i]))
        linha[2].markdown('##### {}'.format(prog_df['capitulos_lidos'][i]))

        if 0 < prog_df['percentual'][i] < 1:
            labels = [
                '##### {}%'.format(round(prog_df['percentual'][i] * 100, 2)),
                ':rocket:',
            ]
        elif prog_df['percentual'][i] == 1:
            labels = ['##### 100%', ':star:']
        else:
            labels = ['', '']

        linha[3].write(labels[0])
        linha[4].progress(prog_df['percentual'][i])
        linha[5].write(labels[1])
