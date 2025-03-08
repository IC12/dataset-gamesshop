## Como seria a estrutura do projeto em Python:

| Pasta/Arquivo                            | Descrição                                                   |
|------------------------------------------|-------------------------------------------------------------|
| **/projeto_analise_vendas**              | Diretório principal do projeto                              |
| **/data**                                | Pasta para armazenar os arquivos CSV                        |
| Meganium_Sales_Data_-_AliExpress.csv     | Arquivo de dados de vendas da AliExpress                     |
| Meganium_Sales_Data_-_Etsy.csv           | Arquivo de dados de vendas da Etsy                           |
| Meganium_Sales_Data_-_Shopee.csv         | Arquivo de dados de vendas da Shopee                         |
| **/src**                                 | Código-fonte do projeto                                      |
| __init__.py                              | Arquivo de inicialização do módulo                           |
| main.py                                  | Arquivo principal que executa as análises                    |
| config.py                                | Configurações globais, como caminhos dos arquivos           |
| loader.py                                | Carrega e processa os arquivos CSV                          |
| analysis.py                              | Contém as funções de análise de dados                        |
| visualization.py                         | Contém funções para gerar gráficos                           |
| **/outputs**                             | Pasta para salvar gráficos gerados                           |
| vendas_por_pais.png                      | Gráfico de vendas por país                                   |
| idade_media_por_pais.png                 | Gráfico de idade média por país                              |
| requirements.txt                         | Dependências do projeto (pandas, matplotlib, seaborn)        |
| README.md                                | Explicação sobre como rodar o projeto                        |
