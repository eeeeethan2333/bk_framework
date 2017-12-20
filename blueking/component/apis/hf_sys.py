from ..base import ComponentAPI


class CollectionsHFSys(object):
    """Collections of HF SYS APIS"""

    def __init__(self, client):
        self.client = client

        self.get_data = ComponentAPI(
            client=self.client, method='GET', path='/api/c/self-service-api/hf_system/get_data/',
            description=u'hf get data',
        )
