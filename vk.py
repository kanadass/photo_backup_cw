import requests


class VK:

    base_url = 'https://api.vk.com/method/'

    def __init__(self, access_token, version='5.131'):
        self.params = {
            'access_token': access_token,
            'v': version
        }

    def get_photos(self, user_id, count):
        vk_api_url = f'{self.base_url}photos.get'
        params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'photo_sizes': 1,
            'extended': 1,
            'count': count,
            **self.params
        }
        response = requests.get(vk_api_url, params=params)
        data = response.json()
        if 'response' in data:
            return data['response']['items']
        else:
            print('Failed to upload the photo from VK.')



