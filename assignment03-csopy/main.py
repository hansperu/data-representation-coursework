import requests

def download_dataset(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'w') as file:
            file.write(response.text)
    else:
        print(f"Failed to download data: {response.status_code}")

if __name__ == "__main__":
    url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
    file_name = "cso.json"
    download_dataset(url, file_name)
