# Databricks

Databricks é uma plataforma de análise de dados aberta e unificada para engenharia de dados, ciência de dados, aprendizado de máquina e análise. Feita pelos criadores originais do Apache Spark TM , Delta Lake, MLflow e Koalas.

Utilizado para:
*    AWS
*    Microsoft Azure
*    Google Cloud

## Criação de Cluster

É no cluster que ficará os ambientes do python, haddop e spark.
Para criar:
*   Clicar em Computer 
*   Clicar em Create compute
*   Dar nome e deixar na versão mais atual

**OBS:** O cluster demora um pouco para ser criado.

![Cluster 01](./imagem/Cria%C3%A7%C3%A3o%20do%20Cluster/imagem-1.jpg)
![Cluster 02](./imagem/Cria%C3%A7%C3%A3o%20do%20Cluster/imagem-2.jpg)
![Cluster 03](./imagem/Cria%C3%A7%C3%A3o%20do%20Cluster/imagem-3.jpg)

## Envio de Arquivos

Em settings, clicar em Admin Console. Ativar o DBFS no worspace.
Após atualizar a página, clicar em Data, DBFS, FileStore, Tables, Upload e subir um arquivo (csv, json...)
![Data](./imagem/Envio%20de%20arquivos/imagem-1.jpg)

## Criar um notebook

Na aba de menu, clicar em Workspace, Users, selecionar seu usuário.
Clicar com o botão direito na página e selecionar create e depois notebook.

**SEMPRE** será necessário ter um **cluster ativo** para rodar o código.
![Notebook 1](./imagem/Cria%C3%A7%C3%A3o%20do%20Notebook/imagem-1.jpg)
![Notebook 2](./imagem/Cria%C3%A7%C3%A3o%20do%20Notebook/imagem-2.jpg)

Para trocar o **tema do notebook**: Clicar em View, Theme e Dark Theme