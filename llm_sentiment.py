# This script goes through all speeches in the 'ev_speeches' collection and asks the AI if the speech is positive, negative or neutral towards electric vehicles.
# It also asks the AI to list all arguments related to electric vehicles in the speech and to give a detailed summary of what is said about electric vehicles in the speech.

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

    speech['llm_sentiment'] = sentiment.lower()

    prompt = f'''In the speech below something related to electric vehicles is mentioned.\n
    """{text}"""\n
    Please give me a list of all arguments related to electric vehicles in the text above. One argument per line.
    Answer ONLY with the arguments, no greeting or explanation. Keep to the information in the text.
    '''
    arguments = ollama.generate(prompt=prompt)
    arguments_list = arguments.split('\n')
    speech['llm_arguments'] = arguments_list

    prompt = f'''In the speech below something related to electric vehicles is mentioned.\n
    """{text}"""\n
    What is said about electric vehicles in the text above? Give me a detailed summary and keep to the information in the text.
    '''
    summary = ollama.generate(prompt=prompt)
    speech['llm_summary'] = summary

    arango.update_ev_document(speech)
