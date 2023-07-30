import os
from vk import VK
from ya_disk import YaDisk
import json
from datetime import datetime
from tqdm import tqdm
from dotenv import load_dotenv


def main():
    vk_user_id = input('Enter VK user ID (only digits): ')
    num_photos = int(input('Enter the number of photos to save (default is 5): ') or 5)

    load_dotenv()
    token_ya = os.getenv('ya_token')
    token_vk = os.getenv('vk_token')

    try:
        vk = VK(token_vk)
        photos = vk.get_photos(vk_user_id, count=num_photos)
        result = []

        ya_disk = YaDisk(token_ya)
        folder_name = f'VK_Photos_{vk_user_id}'
        ya_disk.create_folder(folder_name)

        for photo in tqdm(photos, desc='Uploading photos', unit='photo', ncols=80):
            likes = photo['likes']['count']
            date = datetime.fromtimestamp(photo['date']).strftime('%Y-%m-%d')
            file_name = f'{likes}_{date}.jpg'
            photo_url = photo['sizes'][-1]['url']

            if ya_disk.upload_photo(folder_name, file_name, photo_url):
                result.append({
                    'file_name': file_name,
                    'size': 'z',
                })

        with open('result.json', 'w') as json_file:
            json.dump(result, json_file, ensure_ascii=False, indent=4)

        print(f'The photos has been successfully uploaded to Yandex.Disk.')

    except Exception as e:
        print(f'An error occurred. {str(e)}')

if __name__ == '__main__':
    main()
