import requests


class YaDisk:

    base_url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, folder_name):
        yandex_api_url = f'{self.base_url}resources'
        headers = self.get_headers()
        params = {
            'path': folder_name
        }

        response = requests.put(yandex_api_url, headers=headers, params=params)
        if response.status_code == 201:
            return True
        elif response.status_code == 409:
            print('The folder already exists on Yandex.Disk.')
            return True
        else:
            print('Failed to create folder on Yandex.Disk.')

    def upload_photo(self, folder_name, file_name, file_url):
        yandex_api_url = f'{self.base_url}resources/upload'
        headers = self.get_headers()
        params = {
            'path': f'{folder_name}/{file_name}',
            'url': file_url,
            'overwrite': False
        }

        response = requests.post(yandex_api_url, headers=headers, params=params)
        data = response.json()

        if 'href' in data:
            return True
        elif response.status_code == 409:
            print(f'The file {file_name} already exists on Yandex.Disk.')
        else:
            print(f'Failed to upload photo to Yandex.Disk: {data}')




