# Análise de Vendas de Propriedades em Nova York

## Descrição

Esta aplicação interativa permite explorar e visualizar dados de vendas de propriedades na cidade de Nova York. Utilizando um dataset detalhado, você pode analisar as tendências de preço, a distribuição por bairros e muito mais. O aplicativo oferece gráficos e tabelas para facilitar a análise dos dados de vendas de imóveis.

## Funcionalidades

- **Seleção de Mês:** Escolha o mês desejado na barra lateral para filtrar os dados de vendas de propriedades.
- **Visualização de Dados:** Veja os dados de uma coluna específica e a visualização completa dos dados filtrados.
- **Gráficos Interativos:**
  - **Preço por Dia:** Variação dos preços de venda das propriedades ao longo dos dias do mês selecionado.
  - **Distribuição dos Preços por Bairro (Box Plot):** Distribuição dos preços de venda das propriedades em diferentes bairros.
  - **Preço Total por Classe de Edifício (Barra Empilhada):** Preço total de venda das propriedades agrupadas por categoria de classe de edifício.
  - **Preço Total por Bairro:** Preço total de venda das propriedades em cada bairro.
  - **Distribuição de Preço por Bairro (Pizza):** Proporção do preço total de venda das propriedades em cada bairro.
  - **Regressão de Preço por Área do Terreno:** Relação entre o preço de venda das propriedades e a área do terreno.
  - **Série Temporal do Preço Médio:** Variação do preço médio de venda das propriedades ao longo do tempo.

## Observação sobre os Bairros

No dataset, os bairros são representados por códigos numéricos:
- 1: Manhattan
- 2: Bronx
- 3: Brooklyn
- 4: Queens
- 5: Staten Island

Estes códigos foram substituídos pelos nomes dos bairros para facilitar a interpretação dos dados.

## Instruções de Uso

1. **Instalação:** Certifique-se de que você tem o Python e o Streamlit instalados. Se não, você pode instalar o Streamlit usando o comando `pip install streamlit`.

2. **Autenticação Kaggle:** Configure sua autenticação Kaggle com a API do Kaggle. Você precisa do seu arquivo `kaggle.json` para autenticação.

3. **Executar o Aplicativo:**
   - Coloque o arquivo `kaggle.json` no diretório `.kaggle` (se ainda não estiver lá).
   - Execute o comando a seguir no terminal para iniciar o aplicativo. Substitua `app.py` pelo nome do seu arquivo Python.
     ```bash
     streamlit run app.py
     ```     

4. **Observação sobre Ambiente Virtual:** É recomendável usar um ambiente virtual para evitar conflitos de dependências e garantir um ambiente limpo. Você pode criar um ambiente virtual com:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

5. **Exploração dos Dados:** Use a barra lateral para selecionar o mês desejado e explore as diferentes visualizações e gráficos interativos.

## Tecnologias Utilizadas

- **Streamlit:** Framework para criação de aplicativos web interativos em Python.
- **Pandas:** Biblioteca para manipulação e análise de dados.
- **Plotly Express:** Biblioteca para criação de gráficos interativos.
- **Kaggle API:** Para download do dataset.

## Autora
Este projeto tem fins educativos e foi idealizado por Eduarda Figueredo.
