from src.authorized_api_call import authorized_api_call
from src.config import config
from src.pretty_print import pretty_print


def list_vendor() -> None:
    url = f'{config.pub_server}/api/v1/vendor/list'
    response = authorized_api_call(
        url,
        orgId=config.org_id,
    )
    pretty_print(response)


if __name__ == '__main__':
    list_vendor()
