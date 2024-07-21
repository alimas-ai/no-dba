# 1. Cargar la bbdd con langchain
#from langchain.sql_database import SQLDatabase
from langchain_community.utilities import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///ecommerce.db")

# 2. Importar las APIs
import a_env_vars
import os
os.environ["OPENAI_API_KEY"] = a_env_vars.OPENAI_API_KEY

# 3. Crear el LLM
#from langchain.chat_models import ChatOpenAI
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0,model='gpt-3.5-turbo')

# 4. Crear la cadena
#from langchain import SQLDatabaseChain
#from langchain.chains.sql_database import SQLSQLDatabaseChain
from langchain_experimental.sql import SQLDatabaseChain

cadena = SQLDatabaseChain(llm = llm, database = db, verbose=False)

# 5. Formato personalizado de respuesta
formato = """
Data una pregunta del usuario:
1. crea una consulta de sqlite3
2. revisa los resultados
3. devuelve el dato
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
#{question}
5. al final del texto devuelto muestra la consulta de sqlite3 que se genero
"""

# 6. Función para hacer la consulta

def consulta(input_usuario):
    consulta = formato.format(question = input_usuario)
    resultado = cadena.run(consulta)
    print("la consulta es: %s" % consulta)
    print("el resultado es: %s" % resultado)
    return(resultado)
