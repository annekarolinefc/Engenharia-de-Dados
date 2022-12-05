# Apache Spark

## Spark
É uma ferramenta de Processamento de Dados Distribuído e um Cluster.

* Trabalha em **Mémória**
* É altamente **veloz**
* É **escalável** - aumenta a capacidade a medida que você necessita de mais capacidade para processamento - adiciona nós (computadores)
* O Spark escala horizontalmente (clusters)
* Permite a replicação / tolerância a falhas: os dados são copiados entre os nós do cluster. Isso traz o benefício de, entre outras coisas, **tolerância a falhas**.
* Arquitetura voltada para processar dados. Melhor performance, porem nao substitui Python e não substitui o SQL ou um SGBDR.

### Particionamento
Executer -> Jan 2022
Executer -> Fev 2022
Executer -> Mar 2022

### Linguagens
* Scala
* Python
* Java
* R
* SQL

### Componentes do Spark
* Machine Learning (MLib)
* SQL (Spark SQL)
* Processamento em Streaming
* Processamento de Grafos (GraphX)

### Elementos
* Spark Session : Seção
* Aplication: Programa

### Transformações e Ações
Um dataframe é imutável: traz tolerância a falha
Uma transformação gera um novo dataframe.
O processamento de transformações de fato só ocorre quando há uma ação: Lazy Evaluation.

Dataframe DF ...

Transformação - registra a transformação, mas nao executa.
* filter
* union
* sample

Ação:
* show
## Sobre os Dados
Os dados são observados por dois aspectos principais:
* Armazenamento
* Processamento

### Processamento de dados

Processamos os dados para **produzir valor**, isto é, geram informação e conhecimento.

Processar os dados requer poder computacional:
* CPU
* Memória
* Disco

Portanto, quanto mais dado você tem, mais poder computacional você precisa (**CUSTO COMPUTACIONAL**)

Era do Big Data - tudo produz dado.

## Spark SQL
Permite ler dados tabulares de várias fontes (CSV, Json, Parquet, ORC e etc)
Pode usar sintaxe SQL