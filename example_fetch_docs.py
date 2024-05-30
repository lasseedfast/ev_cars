# Example of fetching documents and go though them one by one using Ollama:

from arango_class import ArangoDB
from ollama_class import Ollama


# Get the documents where "electric car" is mentioned
arango = ArangoDB()
db = arango.db
q = 'FOR doc IN speeches FILTER doc.translation LIKE "%electric car%" RETURN doc'
cursor = db.aql.execute(q) # Modify query
documents = list(cursor)


# Go though the documents one by one
ollama = Ollama()

for doc in documents:
    text = doc['translation']
    prompt =f"""Below is a transcript of a speech given in the European Parliament. I'm interested in all arguments related to electric cars. 
    \n{text}\n
        Please give me a list of all arguments related to electric cars in the text above. One argument per line.
Answer ONLY with the arguments. Kepp to the information in the text.""" #TODO Make a better prompt!
    
    arguments = ollama.generate(prompt)
