from pprint import pprint

import requests


def client():
    token = "Token 278aef4e10ac0ed957b7395ca68274d7140f8ad6"

    headers = {
        "Authorization": token,
    }

    response = requests.get(
        url="http://127.0.0.1:8000/api/kullanici-profilleri",
        headers=headers,
    )

    print(f"Status Code: {response.status_code}")

    response_data = response.json()
    pprint(response_data)


if __name__ == "__main__":
    client()
