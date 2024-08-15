import streamlit as st
import pandas as pd
import plotly.express as px
import zipfile
import os
from kaggle.api.kaggle_api_extended import KaggleApi

st.set_page_config(layout="wide")

st.title("Análise de Vendas de Propriedades em Nova York")
st.markdown("""
Este aplicativo interativo permite explorar e visualizar dados de vendas de propriedades na cidade de Nova York. 
Utilizando um dataset detalhado, você pode analisar as tendências de preço, distribuição por bairros e muito mais.
Selecione o mês desejado na barra lateral para começar a explorar.
""")

st.markdown("""
**Observação sobre os Bairros:**
No dataset, os bairros são representados por códigos numéricos:
- 1: Manhattan
- 2: Bronx
- 3: Brooklyn
- 4: Queens
- 5: Staten Island
""")

api = KaggleApi()
api.authenticate()

dataset = 'new-york-city/nyc-property-sales'
zip_file = 'nyc-property-sales.zip'  

api.dataset_download_files(dataset, path='.', unzip=False)

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall('nyc_property_sales')

extracted_files = os.listdir('nyc_property_sales')
st.write("Arquivos extraídos:", extracted_files)

csv_file_name = None
for file in extracted_files:
    if file.endswith('.csv'):
        csv_file_name = file
        break

if csv_file_name is None:
    st.error("Nenhum arquivo CSV encontrado no diretório extraído.")
    st.stop()

csv_file_path = os.path.join('nyc_property_sales', csv_file_name)

if not os.path.isfile(csv_file_path):
    st.error(f"O arquivo {csv_file_path} não foi encontrado.")
    st.stop()

df = pd.read_csv(csv_file_path)

if 'SALE DATE' in df.columns:
    df['SALE DATE'] = pd.to_datetime(df['SALE DATE'], errors='coerce')
    df = df.dropna(subset=['SALE DATE']) 
    df['Month'] = df['SALE DATE'].apply(lambda x: str(x.year) + "-" + str(x.month))
    month = st.sidebar.selectbox("Mês", df["Month"].unique())
    df_filtered = df[df["Month"] == month]

    if 'LAND SQUARE FEET' in df.columns:
        df_filtered['LAND SQUARE FEET'] = pd.to_numeric(df_filtered['LAND SQUARE FEET'], errors='coerce')
        df_filtered = df_filtered.dropna(subset=['LAND SQUARE FEET'])  
    
    if 'SALE PRICE' in df.columns:
        df_filtered['SALE PRICE'] = pd.to_numeric(df_filtered['SALE PRICE'], errors='coerce')
        df_filtered = df_filtered.dropna(subset=['SALE PRICE'])  

    borough_map = {
        1: 'Manhattan',
        2: 'Bronx',
        3: 'Brooklyn',
        4: 'Queens',
        5: 'Staten Island'
    }

    if 'BOROUGH' in df.columns:
        df_filtered['BOROUGH'] = df_filtered['BOROUGH'].map(borough_map)

    col1, col2 = st.columns([1, 2])  

    with col1:
        column_to_view = st.selectbox("Selecione uma coluna para visualizar os dados:", df.columns)
        st.write(f"Dados da coluna **{column_to_view}**:")
        st.write(df[column_to_view])

    with col2:
        st.write("Visualização Completa dos Dados Filtrados")
        st.dataframe(df_filtered)

    # Gráficos
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5 = st.columns(1)[0]  

    # Gráfico de preço por dia
    if 'SALE PRICE' in df.columns:
        
        fig_date = px.bar(df_filtered, x="SALE DATE", y="SALE PRICE", color="BOROUGH", title="Preço por Dia")
        col1.plotly_chart(fig_date, use_container_width=True)

    # Gráfico de Preço por Bairro (Box Plot)
    if 'SALE PRICE' in df.columns:
        fig_price_by_borough = px.box(df_filtered, x="BOROUGH", y="SALE PRICE", title="Distribuição dos Preços por Bairro")
        col2.plotly_chart(fig_price_by_borough, use_container_width=True)

    # Gráfico de Preço Total por Classe de Edifício (Barra Empilhada)
    if 'BUILDING CLASS CATEGORY' in df.columns:
        building_class_total = df_filtered.groupby("BUILDING CLASS CATEGORY")[["SALE PRICE"]].sum().reset_index()
        fig_building_class = px.bar(building_class_total, x="BUILDING CLASS CATEGORY", y="SALE PRICE", title="Preço Total por Classe de Edifício", color="BUILDING CLASS CATEGORY", text="SALE PRICE")
        col5.plotly_chart(fig_building_class, use_container_width=True)

    # Preço total por bairro
    if 'BOROUGH' in df.columns:
        borough_total = df_filtered.groupby("BOROUGH")[["SALE PRICE"]].sum().reset_index()
        fig_borough_total = px.bar(borough_total, x="BOROUGH", y="SALE PRICE", title="Preço Total por Bairro")
        col4.plotly_chart(fig_borough_total, use_container_width=True)

    # Gráfico de pizza - Distribuição de Preço por Bairro
    if 'BOROUGH' in df.columns:
        borough_price_distribution = df_filtered.groupby("BOROUGH")[["SALE PRICE"]].sum().reset_index()
        fig_pie = px.pie(borough_price_distribution, values="SALE PRICE", names="BOROUGH", title="Distribuição de Preço por Bairro")
        col3.plotly_chart(fig_pie, use_container_width=True)
        
    # Análise de regressão
    if 'LAND SQUARE FEET' in df_filtered.columns and 'SALE PRICE' in df_filtered.columns:
        fig_regression = px.scatter(df_filtered, x="LAND SQUARE FEET", y="SALE PRICE", trendline="ols", title="Regressão de Preço por Área do Terreno")
        st.plotly_chart(fig_regression, use_container_width=True)

    # Análise de séries temporais
    if 'SALE DATE' in df.columns and 'SALE PRICE' in df.columns:
        df_time_series = df_filtered.groupby('SALE DATE')['SALE PRICE'].mean().reset_index()
        fig_time_series = px.line(df_time_series, x="SALE DATE", y="SALE PRICE", title="Série Temporal do Preço Médio")
        st.plotly_chart(fig_time_series, use_container_width=True)

else:
    st.error("O arquivo CSV não contém uma coluna de data esperada.")
