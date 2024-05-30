from arango_class import ArangoDB
from ollama_class import Ollama
arango = ArangoDB()
db = arango.db

ollama = Ollama()

# Get all speeches from the 'ev_speeches' collection, containing the 400 speeches filtered out from the European Parliament
speeches = arango.all_ev_speeches()

negative_arguments = []
positive_arguments = []
neutral_arguments = []

for speech in speeches:
    if speech['llm_sentiment'] == 'negative':
        negative_arguments.extend(speech['llm_arguments'])
    elif speech['llm_sentiment'] == 'positive':
        positive_arguments.extend(speech['llm_arguments'])
    else:
        neutral_arguments.extend(speech['llm_arguments'])

negative_arguments = list(set(negative_arguments))
positive_arguments = list(set(positive_arguments))
neutral_arguments = list(set(neutral_arguments))


for sentiment, arguments in zip(['negative', 'positive', 'neutral'], [negative_arguments, positive_arguments, neutral_arguments]):
    prompt = f'''Below is a list of arguments related to electric vehicles. They are mostly {sentiment} towards electric vehicles.
    \n{negative_arguments}\n
    What arguments are there? Give me a list where you group the arguments into categories.
    Answer ONLY with the grouped arguments, no greeting or explanation. Keep to the information in the list above.
    '''
    grouped_arguments = ollama.generate(prompt=prompt)
    print(sentiment.upper())
    print(grouped_arguments)
    print('-'*30)