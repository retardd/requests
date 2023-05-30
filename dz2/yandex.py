import requests

URL = 'https://cloud-api.yandex.net/'

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, remote_file_path: str):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        temp_check = requests.get(f'{URL}v1/disk/resources?path={remote_file_path}',
                                   headers=headers).json()
        if temp_check.get('error') == 'DiskNotFoundError':
            res = requests.put(f'{URL}v1/disk/resources?path={remote_file_path}', headers=headers)
            print(res)
        with open(file_path, 'rb') as f:
            try:
                res = requests.get(f'{URL}v1/disk/resources/upload?path={remote_file_path}/{f.name}&overwrite=false',
                                   headers=headers).json()
                res = requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input()
    remote_file_path = input()
    token = input()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, remote_file_path)