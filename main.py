import requests

urls = [
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts",
    "https://httpstat.us/500"
]

print("\n--- API Health Check ---\n")

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code

        if status == 200:
            print(f"{url} -> OK ({status})")
        else:
            print(f"{url} -> WARNING ({status})")

    except requests.exceptions.RequestException:
        print(f"{url} -> ERROR (request failed)")
