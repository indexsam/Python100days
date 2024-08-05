import requests


class Post:
 
    def get_url() -> list:
        response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()
        data = response.json()

        return data