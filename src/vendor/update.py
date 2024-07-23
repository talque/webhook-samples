from src.authorized_api_call import authorized_api_call
from src.config import config
from src.pretty_print import pretty_print
from src.file.upload import upload_file


def update_vendor() -> None:
    url = f'{config.api_server}/webhook/org/{config.org_id}/vendor/update'
    photo = upload_file('assets/test.jpg')
    response = authorized_api_call(
        url,
        extId='myVendorId123',
        name={
            'EN_US': 'My Updated Sample Vendor',
        },
        photo=photo,
        clearGallery=False,    # each update adds same image
        gallery=[{
            'action': 'ADD_IMAGE',
            'tempFileId': upload_file('assets/test.jpg'),
            'name': 'added_image.jpg',
        }],
        clearPortfolio=False,    # each update adds same image
        portfolio=[{
            'action': 'ADD_DOCUMENT',
            'name': 'document.txt',
            'title': {
                'EN_US': 'Added document',
            },
            'tempFileId': upload_file('assets/document.txt'),
        }],
    )
    pretty_print(response)


if __name__ == '__main__':
    update_vendor()
