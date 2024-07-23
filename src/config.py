import dataclasses


@dataclasses.dataclass(frozen=True)
class Config(object):

    api_server: str
    pub_server: str
    org_id: str
    api_client_id: str
    api_client_secret: str


config = Config(
    # Dev server
    # api_server='http://localhost:8080',
    # pub_server='http://localhost:8081',

    # Production server
    api_server='https://www.talque.com',
    pub_server='https://event.talque.com',
    
    # Settings specific to your event
    org_id='grYbXNMwgkLIyJnnO546',
    api_client_id='o3kjjdQmalnHeaVc2Bj0',
    api_client_secret='NYVyRy1yUwwJ5yQwv2Tu',
)
