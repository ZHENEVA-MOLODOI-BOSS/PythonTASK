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
