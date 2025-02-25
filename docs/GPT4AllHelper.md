# GPT4All

In deze folder vindt je een helper-klasse voor GPT4All. Hiermee kun je toegang krijgen 
tot veel bestaande taalmodellen. De server hiervoor draai je op je eigen computer. 

Er is goed en slecht nieuws: het goede nieuws is dat al je chats privé blijven. 
Het slechte nieuws is dat het je flink wat RAM gaat kosten. 

Om je op weg te helpen met deze hulpcode, kun je  de volgende stappen volgen.

## Een taalmodel kiezen

De keuze voor een taalmodel zal in veel gevallen bepaald worden door 
de limitaties van je computer. Het zijn flink zware modellen. Houd er ook rekening 
mee dat ze moeten kunnen draaien op de computer van je teamgenoten.

Llama 3 is gemaakt door Meta en Open-Source en ons uitgangspunt voor dit voorbeeld. 
Je kunt deze ook krijgen in 3 varianten, van erg zwaar voor je computer tot een stuk 
beter te doen.

- Llama 3 8B parameters, vereist 8GB RAM
- Llama 3 3B parameters, vereist 4GB RAM
- Llama 3 1B parameters, vereist 1GB RAM

## Installatie

1. Begin met GPT4All te installeren op je eigen computer, via https://gpt4all.io/index.html?ref=localhost
2. Installeer het gewenste taalmodel op je computer. Deze zal automatisch ook gebruikt worden 
voor de server, als het gevraagde taalmodel niet beschikbaar is.
3. Download eventueel nog andere taalmodellen om te gebruiken.
4. Ga naar de Instellingen, naar het kopje Advanced en selecteer `Enable Local API Server`.
5. Restart nu het programma

![GPT4All interface screenshot](gpt4all_local_api.png)

Als het goed is heb je nu een lokale API server runnen. Je kunt hiervan de poort eventueel 
aanpassen, maar als je dat niet gedaan hebt, moet je nu een response kunnen krijgen van de API 
door de volgende link in je browser te plakken:

`http://localhost:4891/v1/models`

Zie je een response? Dan ben je klaar om te gaan! Hier kun je ook meteen de modellen zien 
die beschikbaar zullen zijn voor je avonturen.

## Het model configureren

Het model heeft drie opties om te configureren:

1. Het taalmodel om te gebruiken. Dit hebben we al even behandeld bij [de sectie over een taalmodel kiezen](#een-taalmodel-kiezen).
2. Het maximale aantal tokens. Dit hangt af van hoe lang je response moet zijn. Hoe meer tokens, hoe
langer het antwoord van het taalmodel. (Tip: https://www.datacamp.com/blog/what-is-tokenization)
3. De temperatuur bepaalt hoe 'creatief' het model mag zijn. Een temperatuur dicht bij de 0 geeft het 
meest waarschijnlijke antwoord, maar wordt dan wel snel repetitief, waardoor we soms een betere oplossing 
kunnen missen. Een hogere temperatuur zorgt voor meer willekeur (randomness) in de antwoorden. (Tip: https://www.hopsworks.ai/dictionary/llm-temperature)

Maar, configureren hoeft niet per se, ik heb in de helper-code al wat typische waarden voor jullie meegegeven. 
Het model kunnen we met Python aanmaken als standaard-model, of met onze eigen instellingen.

Standaardinstellingen:
```py
# Defaults: Llama 3.2 1B Instruct if installed, 50 max tokens and a temperature of 0.28
gpt: GPT4AllHelper = GPT4AllHelper()
```

Eigen model, maximaal aantal tokens of temperatuur:
```py
# We set our own values to customize the model :)
gpt: GPT4AllHelper = GPT4AllHelper(model="Llama 3 8B Instruct", max_tokens=200, temperature=0.4)
```

Alle parameters zijn optioneel en kunnen dus eventueel weggelaten worden.

Volledige voorbeeldcode om te prompten en modellen op te vragen:

```py
# Let goed op waar je de helper in je eigen project plaatst
from extra.GPT4All.GPT4AllHelper import *

# Example prompt
example_prompt: str = "Who is Lionel Messi?"
# Create a default GPT
gpt: GPT4AllHelper = GPT4AllHelper()

# Ask which models are available
models_response = gpt.get_models()
print(f"Available models response:\n{models_response}")

# Send our example prompt to the language model and get a response :D
example_response = gpt.post(example_prompt)

# Print some information about the response
print(f"API responded with {example_response.status_code}")
print(f"JSON response:\n{example_response.json()}")
```