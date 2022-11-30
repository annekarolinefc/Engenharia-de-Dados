from pyspark import spark
path = '../Conjunto de Dados/VACINAS.csv'
formato = "csv"

# Criando um DataFrame a partir de um csv
df_vacinas = spark.read.format(formato)\
    .option('header', 'true')\
    .option('sep', ':')\
    .option('inferSchema', 'true')\
    .load(path)
    
df_vacinas.display()