from arango_class import ArangoDB
from ollama_class import Ollama

# Initialize the Ollama class to use for questions to AI
ollama = Ollama()

# Get the connection to the Arango DB
arango = ArangoDB()
db = arango.db

# Get all speeches from the 'ev_speeches' collection, containing the 400 speeches filtered out from the European Parliament
speeches = arango.all_ev_speeches()

# Go through each speech and ask the AI if the speech is positive, negative or neutral towards electric vehicles
for speech in speeches:
    text = speech['text']
    prompt = f'''In the speech below something related to electric vehicles is mentioned.\n
    """{text}"""\n
    Is the speech positive, negative or neutral when it comes to electric vehicles?
    Asnwer ONLY with 'positive', 'negative' or 'neutral', NOTHING else.
    '''
    sentiment = ollama.generate(prompt=prompt)
    speech['sentiment'] = sentiment
    arango.update_ev_document(speech)
