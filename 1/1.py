import json

import requests


class JSONPLaceHolderAPI:
    base_url = "https://jsonplaceholder.typicode.com"

    @classmethod
    def get_posts(cls, endpoint: str = "/posts"):
        response = requests.get(cls.base_url + endpoint)
        return response.json()

    @classmethod
    def save_json(cls, filename: str, data: dict) -> None:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)



if __name__ == "__main__":
    data = JSONPLaceHolderAPI.get_posts()
    JSONPLaceHolderAPI.save_json("data.json", data)