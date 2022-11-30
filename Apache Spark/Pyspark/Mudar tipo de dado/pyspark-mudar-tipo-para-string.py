df.printSchema()
df = df.withColumn('ID', df['ID'].cast('string'))
df.printSchema()