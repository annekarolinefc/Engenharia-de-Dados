from pyspark.sql.functions import split 

df_teste = df\
    .select('Carimbo de data/hora')\
    .withColumn('dia', split(df['Carimbo de data/hora'], '/').getItem(0))\
    .withColumn('mes', split(df['Carimbo de data/hora'], '/').getItem(1))

df_teste.show(5)