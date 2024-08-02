# =======================================================
# Imports
# =======================================================

import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt

# =======================================================
# Datasets
# =======================================================
df_acidentes_uf_geral = pd.read_csv('acidentes_por_uf_geral.csv', sep=',', encoding="ISO-8859-1")
df_acidentes_tipo_geral = pd.read_csv('acidentes_por_tipo_geral.csv', sep=',', encoding="UTF-8")
df_acidentes_br_geral = pd.read_csv('acidentes_por_br_geral.csv', sep=',', encoding="ISO-8859-1")
df_acidentes_causa_geral = pd.read_csv('acidentes_por_causa_geral.csv', sep=',', encoding="UTF-8")

# rankings
df_ranking_uf = pd.read_csv('ranking_acidentes_uf.csv', sep=',', encoding="UTF-8")
df_ranking_tipo = pd.read_csv('ranking_acidentes_tipo.csv', sep=',', encoding="UTF-8")
df_ranking_br = pd.read_csv('ranking_acidentes_br.csv', sep=',', encoding="UTF-8")

# =======================================================
# Funções
# =======================================================
def agrupamento_acidentes_por_ano_por_uf(df):
  contagem_por_uf = df['uf'].value_counts().reset_index()
  contagem_por_uf.columns = ['UF', 'Qtd']
  return contagem_por_uf
# =======================================================
def gera_grafico_por_uf(ano, contagem_por_uf_ano):

  lista_cores = alt.Scale(domain= contagem_por_uf_ano['UF'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_uf = alt.Chart(contagem_por_uf_ano).mark_bar().encode(
      y=alt.Y('UF:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('Qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['UF', 'Qtd'],
      color=alt.Color('UF:N', scale=lista_cores)

  ).properties(
      title=f'Acidentes por UF em {ano}'
  ).interactive()

  return chart_uf
# =======================================================
def contagem_por_tipo_acidente(df_ocorrencia_acidentes):
  contagem_por_tipo = df_ocorrencia_acidentes['tipo_acidente'].value_counts().reset_index(name='qtd').rename(columns={'index': 'UF'})
  contagem_por_tipo.columns = ['tipo_acidente', 'qtd']

  return contagem_por_tipo
# =======================================================
def gera_grafico_por_tipo(ano, contagem_por_tipo_ano):

  lista_cores = alt.Scale(domain=contagem_por_tipo_ano['tipo_acidente'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_tipo = alt.Chart(contagem_por_tipo_ano).mark_bar().encode(
      y=alt.Y('tipo_acidente:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['tipo_acidente', 'qtd'],
      color=alt.Color('tipo_acidente:N', scale=lista_cores)

  ).properties(
      title=f'Acidentes por Tipo no Ano de {ano}',
      width=1024  # Defina a largura em pixels
  ).interactive()

  return chart_tipo
# =======================================================
def gera_grafico_por_br(ano, contagem_por_br_ano):

  lista_cores = alt.Scale(domain=contagem_por_br_ano['br'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_br = alt.Chart(contagem_por_br_ano).mark_bar().encode(
      y=alt.Y('br:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['br', 'qtd'],
      color=alt.Color('br:N', scale=lista_cores)

  ).properties(
      title=f'Acidentes por BR no Ano de {ano}'
  ).interactive()

  return chart_br
# =======================================================
def gera_grafico_por_causa(ano, contagem_por_causa_ano):

  lista_cores = alt.Scale(domain=contagem_por_causa_ano['causa_acidente'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart = alt.Chart(contagem_por_causa_ano).mark_bar().encode(
      y=alt.Y('causa_acidente:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['causa_acidente', 'qtd'],
      color=alt.Color('causa_acidente:N', scale=lista_cores)

  ).properties(
      title=f'Acidentes por Causa no Ano de {ano}',
      width=1024  # Defina a largura em pixels
  ).interactive()


  return chart
# =======================================================

# =======================================================
# Constantes do dashboard
# =======================================================
OPCAO_TODOS = 'Todos'
COLUNA_ANO = 'ano'

st.set_page_config(layout="wide")

# Definir o título fixo para o painel
st.title("Acidentes nas Rodovias Federais do Brasil (2007 a 2023)")

st.sidebar.markdown("# Filtros:")

# Adiciona uma caixa de seleção no sidebar
ano_selecionado = st.sidebar.selectbox(
    'Qual o ano deseja visualizar?',
    (OPCAO_TODOS, '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007')
)

print(ano_selecionado)

meses_selecionados = st.sidebar.multiselect(
    'Quais meses deseja visualizar?',
    [OPCAO_TODOS, 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro','Novembro','Dezembro'],
  )

#st.sidebar.write("Meses selecionados:", meses_selecionados)
print(f'Meses selecionados: {meses_selecionados}')

# Add a slider to the sidebar:
horario_acidente = st.sidebar.slider(
    'Horário do acidente:',
    0, 24, (0, 24)
)

# Definição de abas
# Acidentes por UF | Acidentes por Tipo | Acidentes por BR |
tab01, tab02, tab03, tab04, tab05, tab06, tab07, tab08, tab09 = st.tabs(
  [
    "Acidentes por UF", "Acidentes por Tipo", 
    "Acidentes por BR", "Acidentes por Causa", 
    "Ranking dos Acidentes por UF", "Ranking dos Acidentes por Tipo",
    "Ranking dos Acidentes por BR", "Ranking dos Acidentes por Causa",
    "Mapa do Brasil"
  ]
)

# ==============================================================================
with tab01:

    # aba 01
    titulo = f'Acidentes por UF ({ano_selecionado})'
    st.markdown(titulo, unsafe_allow_html=True)

    if ano_selecionado != OPCAO_TODOS:
      df_filtrado_uf = df_acidentes_uf_geral[(df_acidentes_uf_geral[COLUNA_ANO] == int(ano_selecionado))]
      grafico_aba_01 = gera_grafico_por_uf(ano_selecionado, df_filtrado_uf)
    else:
      df_filtrado_uf = df_acidentes_uf_geral
      grafico_aba_01 = gera_grafico_por_uf(OPCAO_TODOS, df_filtrado_uf)

    # Exibir o gráfico de barras empilhadas
    st.altair_chart(grafico_aba_01)

# ==============================================================================
with tab02:

  # aba 02
  titulo = f'Acidentes por Tipo ({ano_selecionado})'
  st.markdown(titulo, unsafe_allow_html=True)

  if ano_selecionado != OPCAO_TODOS:
    df_filtrado_tipo = df_acidentes_tipo_geral[(df_acidentes_tipo_geral[COLUNA_ANO] == int(ano_selecionado))]
    grafico_aba_02 = gera_grafico_por_tipo(int(ano_selecionado), df_filtrado_tipo)
  else:
    df_filtrado_tipo = df_acidentes_tipo_geral
    grafico_aba_02 = gera_grafico_por_tipo(OPCAO_TODOS, df_filtrado_tipo)

  # Exibir o gráfico de barras empilhadas
  st.altair_chart(grafico_aba_02)

# ==============================================================================
with tab03:

  # aba 03
  print('Aba 03')
  titulo = f'Acidentes por BR ({ano_selecionado})'
  st.markdown(titulo, unsafe_allow_html=True)

  if ano_selecionado != OPCAO_TODOS:
    df_filtrado_br = df_acidentes_br_geral[(df_acidentes_br_geral[COLUNA_ANO] == int(ano_selecionado))]
    grafico_aba_03 = gera_grafico_por_br(int(ano_selecionado), df_filtrado_br)
  else:
    df_filtrado_br = df_acidentes_br_geral
    grafico_aba_03 = gera_grafico_por_br(OPCAO_TODOS, df_filtrado_br)

  # Exibir o gráfico de barras empilhadas
  st.altair_chart(grafico_aba_03)

# ==============================================================================
with tab04:

  # aba 04
  print('Aba 04')
  titulo = f'Acidentes por Causa ({ano_selecionado})'
  st.markdown(titulo, unsafe_allow_html=True)

  if ano_selecionado != OPCAO_TODOS:
    df_filtrado_causa = df_acidentes_causa_geral[(df_acidentes_causa_geral[COLUNA_ANO] == int(ano_selecionado))]
    grafico_aba_04 = gera_grafico_por_causa(int(ano_selecionado), df_filtrado_causa)
  else:
    df_filtrado_causa = df_acidentes_causa_geral
    grafico_aba_04 = gera_grafico_por_causa(OPCAO_TODOS, df_filtrado_causa)

  # Exibir o gráfico de barras empilhadas
  st.altair_chart(grafico_aba_04)

# ==============================================================================
with tab05:

  # aba 05
  titulo = f'Ranking dos Acidentes por UF entre 2007 e 2023'
  st.markdown(titulo, unsafe_allow_html=True)

  # Ordenar o DataFrame por ano
  df_ordenado_ano = df_ranking_uf.sort_values('ano')

  # Criar o gráfico de linhas interativo
  grafico_aba_05 = alt.Chart(df_ranking_uf).mark_line(point=True).encode(
      x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
      y=alt.Y('Qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
      color='UF:N',
      tooltip=['UF', 'Qtd', 'ano']
  ).properties(
      title='Evolução da Quantidade de Acidentes por UF (2007-2023)',
      width=1024, height=500
  ).add_selection(
      alt.selection_single(fields=['ano'], bind='legend')
  ).interactive()

  st.altair_chart(grafico_aba_05)
  
# ==============================================================================
with tab06:

  # aba 06
  titulo = f'Ranking dos Acidentes por Tipo entre 2007 e 2023'
  st.markdown(titulo, unsafe_allow_html=True)

  # Ordenar o DataFrame por ano
  df_ordenado_ano = df_ranking_uf.sort_values('ano')

  # Criar o gráfico de linhas interativo
  grafico_aba_06 = alt.Chart(df_ranking_tipo).mark_line(point=True).encode(
      x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
      y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
      color='tipo_acidente:N',
      tooltip=['tipo_acidente', 'qtd', 'ano']
  ).properties(
      title='Evolução da Quantidade de Acidentes por Tipo (2007-2023)',
      width=1024, height=500
  ).add_selection(
      alt.selection_single(fields=['ano'], bind='legend')
  ).interactive()

  st.altair_chart(grafico_aba_06)

# ==============================================================================
with tab07:

  # aba 07
  titulo = f'Ranking dos Acidentes por BR entre 2007 e 2023'
  st.markdown(titulo, unsafe_allow_html=True)

  # Ordenar o DataFrame por ano
  df_ordenado_ano = df_ranking_br.sort_values('ano')

  # Criar o gráfico de linhas interativo
  grafico_aba_07 = alt.Chart(df_ranking_br).mark_line(point=True).encode(
      x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
      y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
      color='br:N',
      tooltip=['br', 'qtd', 'ano']
  ).properties(
      title='Evolução da Quantidade de Acidentes por BR (2007-2023)',
      width=1024, height=500
  ).add_selection(
      alt.selection_single(fields=['ano'], bind='legend')
  ).interactive()

  st.altair_chart(grafico_aba_07)

# ==============================================================================
with tab08:

  # aba 08
  titulo = f'Ranking dos Acidentes por Causa entre 2007 e 2023'
  st.markdown(titulo, unsafe_allow_html=True)

with tab09:

  # aba 09
  titulo = f'Mapa do Brasil'
  st.markdown(titulo, unsafe_allow_html=True)

# ==============================================================================
