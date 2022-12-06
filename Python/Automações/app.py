# Permite ir rastreando todo o funcionamento do programa
# Permite encontrar erros, auxiliar tomada de decisão

# cria arquivos txt e vai escrevendo no arquivo tudo e qualquer coisa que a gente quiser, da forma qued a gente quiser. 
# Lemos o registro e entendemos o que aconteceu

# %%
# Biblioteca nativa do Python - não é necessário importa-la
import logging 
LOG_FILENAME = "./Python/Automações/app.log"

logging.basicConfig(filename=LOG_FILENAME,
                    filemode='w',
                    encoding='utf-8', 
                    level = logging.DEBUG
                    #format = "%(asctime)s :: %(levelno)s :: %(lineno)d"
                    )
#logging.basicConfig(filename=LOG_FILENAME,filemode='w',                  level = logging.DEBUG, format = "%(levelname)s %(asctime)s  - %(messsage)s")

#LOG_FORMAT = "%(levelname)s %(asctime)s  - %(messsage)s"
#logging.basicConfig(filename=LOG_FILENAME,filemode='w',                  level = logging.DEBUG, format = LOF_FORMAT)

logging = logging.getLogger()

logging.debug('Essa mensagem irá para o arquivo de log')
logging.warning('Imprime essa mensagem no console')
logging.info('Nao imprime nada no console')
logging.error("mensagem de erro")
logging.critical('Erro grave')
# %%
