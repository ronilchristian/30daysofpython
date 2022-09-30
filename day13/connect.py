import pandas as pd
import pprint
import requests

api_key = "cbff9105301eb47f34178121b9bde957"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYmZmOTEwNTMwMWViNDdmMzQxNzgxMjFiOWJkZTk1NyIsInN1YiI6IjYzMzYxNGVlYTE0YmVmMDA3YTA1Y2UxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-PnENyMoB6746ZB7cuVMNJSimdqEGWCcZ23N0efB3C4"

# Using v3
def get_data(movie_ids):
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    
    data = []
    for movie_id in movie_ids:
        endpoint_path = f"/movie/{movie_id}"
        endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

        r = requests.get(endpoint)
        data.append(r.json())

    return data


# Using v4
# api_version = 4
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# movie_id = 550
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}"
# headers = {"Authorization": f"Bearer {api_key_v4}", "Content-Type": "application/json;charset=utf-8"}

# r = requests.get(endpoint, headers=headers)
# print(r.status_code)
# print(r.text)

# Searching
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "John Wick"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
print(endpoint)

r = requests.get(endpoint)
# print(r.status_code)
# pprint.pprint(r.json())

if r.status_code in range(200, 299):
    data = r.json()
    # print(data.keys())
    results = data["results"]
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = []
        for result in results:
            movie_ids.append(result['id'])
            # print(f"{result['id']} - {result['title']}")



movie_data = get_data(movie_ids)

df = pd.DataFrame(movie_data)
df.to_csv("movies.csv", index=False)
