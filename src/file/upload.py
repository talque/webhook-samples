from typing import Any
from src.authorized_api_call import authorized_api_call
from src.config import config
import logging
from src.pretty_print import pretty_print
import requests


log = logging.getLogger('talque')


def upload_file(filename: str) -> str:
    """
    Upload file and return the new temp file id
    """
    response = create_temp_file_id()
    temp_file_id = response['tempFileId']
    log.debug(f'created temp_file_id={temp_file_id}')
    upload_url = response['uploadUrl']
    upload_file_signed_url(filename, upload_url)
    return temp_file_id


def create_temp_file_id() -> dict[str, Any]:
    """
    Upload file and return the new temp file id
    """
    url = f'{config.api_server}/webhook/file/temp/create'
    response = authorized_api_call(
        url,
    )
    pretty_print(response)
    return response


def upload_file_signed_url(filename: str, upload_url: str) -> None:
    log.debug(f'uploading file {filename} to {upload_url}')
    with open(filename, 'rb') as f:
        content = f.read()
    requests.put(upload_url, data=content, verify=False)


if __name__ == '__main__':
    temp_file_id = upload_file('assets/test.jpg')
    print(temp_file_id)
