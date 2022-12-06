# Importando a Biblioteca
from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
        .appName("Python Spark SQL basic example")\
            .config("spark.some.config.option", "some-value")\
                .getOrCreate() 
                

# Leitura / Criação do DataFrame
df = spark.read.json("examples/people.json")

# Exibição
df.show()