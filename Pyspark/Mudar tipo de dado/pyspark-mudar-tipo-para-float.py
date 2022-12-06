df.printSchema()
df = df.withColumn('ID', df['ID'].cast('float'))
df.printSchema()