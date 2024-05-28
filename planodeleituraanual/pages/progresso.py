import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def index(tab: DeltaGenerator):

    tab.write('## Seu Progresso')
    tab.caption('Acompanhe seu progresso no plano de leitura.')

    prog_df = st.session_state.biblia_df

    prog_df = prog_df.drop(['livro'], axis=1)

    prog_df['percentual'] = [
        prog_df['capitulos_lidos'][i] / prog_df['capitulos'][i]
        for i in range(len(prog_df))
    ]

    tab.progress(
        prog_df['capitulos_lidos'].sum() / prog_df['capitulos'].sum(),
        'Progresso geral',
    )

    tab.divider()

    columns_size = [1, 0.3, 0.4, 0.3, 0.7, 0.1]

    header = tab.columns(columns_size)

    header[0].markdown('#### Livro<br>', unsafe_allow_html=True)
    header[1].markdown('#### Capítulos<br>', unsafe_allow_html=True)
    header[2].markdown('#### Capítulos Lidos<br>', unsafe_allow_html=True)
    header[3].markdown('#### Percentual<br>', unsafe_allow_html=True)
    header[4].markdown('#### Progresso<br>', unsafe_allow_html=True)

    for i in range(len(prog_df)):

        linha = tab.columns(columns_size)
        linha[0].markdown('##### Linha {}'.format(prog_df['id'][i]))
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

    tab.dataframe(prog_df)
