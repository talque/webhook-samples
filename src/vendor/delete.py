from src.authorized_api_call import authorized_api_call
from src.config import config
from src.pretty_print import pretty_print


def delete_vendor() -> None:
    url = f'{config.api_server}/webhook/org/{config.org_id}/vendor/delete'
    response = authorized_api_call(
        url,
        extId='myVendorId123',
    )
    pretty_print(response)


if __name__ == '__main__':
    delete_vendor()
