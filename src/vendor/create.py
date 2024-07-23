from src.authorized_api_call import authorized_api_call
from src.config import config
from src.pretty_print import pretty_print
from src.file.upload import upload_file


def create_vendor() -> None:
    url = f'{config.api_server}/webhook/org/{config.org_id}/vendor/create'
    photo = upload_file('assets/test.jpg')
    response = authorized_api_call(
        url,
        extId='myVendorId123',
        name={'EN_US': 'My Sample Vendor'},
        adminName={'EN_US': 'Internal Name For My Sample Vendor'},
        description={'EN_US': 'Example vendor created via the webhook API'},
        photo=photo,
        backgroundImage=None,
        sponsor=None,
        exhibitor=None,
        perks=[],
    )
    pretty_print(response)


if __name__ == '__main__':
    create_vendor()
