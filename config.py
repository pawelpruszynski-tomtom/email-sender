
class Config:
    """
    The configuration of the 3G statistics process.

    This is encapsulated here so that it can be passed around as a unit and
    mocked for testing.
    """

    def __init__(self):
        """
        Init process configuration.

        Initialise the configuration given a run date (datetime.date), directory
        to put output data (PBFs & split countries) and countries filter (list
        of country codes). The countries filter will be used to limit the set of
        countries that are processed.
        """

        self._smtp_params = {
            'server': 'relay-ams.tomtomgroup.com',
            'port': 25,
            'username': None,
            'password': None,
            'tls': True,
            'send_from': 'MDR IDs generator <mdr_ids_generator@tomtom.com>',
            'success_recipients': [
                'Pawel.Pruszynski@tomtom.com'
            ],
            'success_additional_recipients': [
                'Pawel.Pruszynski@tomtom.com'
            ],
            'failure_recipients': [],
            'failure_additional_recipients': ['Pawel.Pruszynski@tomtom.com']
        }

    def smtp_params(self):
        return self._smtp_params
