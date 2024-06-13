# Python блок.
# На основе открытого API [restcountries.com], предоставляющего подробную информацию о странах мира,
# найти страны соответствующие следующим условиям:
# 1. Русский входит в список государственных языков
# 2. Население страны выше среднего по миру
# В качестве результата необходимо получить список стран и их население [name, population].


import requests

population_list = []
result = []
response = requests.get('https://restcountries.com/v3.1/all').json()

list(map(lambda x: population_list.append(x['population']), response))
avg_population = sum(population_list) / len(population_list) # or np.mean

for item_response in response:
    if item_response['population'] > avg_population and 'rus' in item_response['languages']:
        result.append([item_response['name']['official'], item_response['population']])

print(*result, sep='\n')
