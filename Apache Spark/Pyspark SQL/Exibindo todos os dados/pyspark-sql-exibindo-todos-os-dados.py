df_1.createOrReplaceTempView('TB_Vacinas')

df= spark.sql("""
                SELECT *
                FROM TB_Vacinas
""")

df.display()


#%sql
#SELECT * FROM Tb_Vacinas