# Criação de consultas SQL
Grande parte da rotina de um Engenheiro de Dados é criar consultas com SQL.

Serão consultas destinadas a "**problemas de negócio!**"

Será necessário montar o ambiente para executar as atividades.

Etapas: 
* Criar Cluster Redshift (nome = redshift-cluster-1), ou utilizar um já criado.
* Criar Banco de dados Northwind ( nome = northwind) - (Criar Banco de Dados Nothwind em uma instância Redshift).
* Criar Estrutura do Banco de Dados:
    * Rodar northwindddl.sql utilizando o Editor de Consultas do Redshift.
    * Atente-se para rodar no banco de dados criado.
* Disponibilizar Banco de Dados
* Criar credenciais para Copy (ou utilizar credenciais já existentes)
* Fazer upload dos arquivos csv para um bucket qualquer (serão 8 arquivos csv)
* Executar copy para carregar dados
    Um para cada tabela.  copy.sql pode ser utilizado como modelo.

Os numeros em vermelho são adaptados para sua realidade - Nome tabela = nome arquivo csv

Template: 
```
copy nome
from 'endereco-csv'
CREDENTIALS 'minhas credeciais'
delimiter ';'
region 'minha-regiao-utilizada'
IGNOREHEADER 1
DATEFORMAT AS 'YYYY-MM-DD HH:MI:SS'
```

![imagem](/Desafios/Desafio%2001/imagem.jpg)

Esquema do Banco de Dados:
![bd](/Desafios/Desafio%2001/esquema-bd.jpg) 

Arquivos necessários
* northwindddl.sql
* copy.sql
* Atividade[n].sql
* Dados diversos csv