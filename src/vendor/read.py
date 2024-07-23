from src.authorized_api_call import authorized_api_call
from src.config import config
from src.pretty_print import pretty_print


def read_vendor() -> None:
    url = f'{config.pub_server}/api/v1/vendor/read'
    response = authorized_api_call(
        url,
        orgId=config.org_id,
        vendorIdList=['oo69BSolHxU36yuO6gqA'],
    )
    pretty_print(response)


if __name__ == '__main__':
    read_vendor()
