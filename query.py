def extract_query_parameters(url):
    query_parameters = {}
    if '?' in url:
        query_string = url.split('?')[1]
        parameters = query_string.split('&')
        for parameter in parameters:
            key_value = parameter.split('=')
            if len(key_value) == 2:
                key, value = key_value
                query_parameters[key] = value
    return query_parameters

url = input().strip()
n = int(input())
keys_to_find = [input().strip() for _ in range(n)]

query_params = extract_query_parameters(url)

for key in keys_to_find:
    if key in query_params:
        print(query_params[key])
    else:
        print("-1")
