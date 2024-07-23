from typing import Any
import requests
from src.config import config
import logging


log = logging.getLogger('talque')


def headers() -> dict[str, Any]:
    return {
        'X-TQ-CLIENT-ID': config.api_client_id,
        'X-TQ-SECRET': config.api_client_secret,
        'Content-Type': 'application/json',
    }


def authorized_api_call(url: str, **request_body: Any) -> dict[str, Any]:
    """
    Make api call with authorization and return JSON response
    """
    response = requests.post(url, json=request_body, headers=headers())
    if not response.ok:
        log.error(f'HTTP request failed: {response.text}')
    response.raise_for_status()
    if response.headers.get('Content-Type') != 'application/json; charset=utf-8':
        raise RuntimeError('Expected json respoonse, but got ' + response.text)
    return response.json()
