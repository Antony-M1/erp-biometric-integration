# ERPNext related configs
ERPNEXT_API_KEY = 'my_api_key'
ERPNEXT_API_SECRET = 'my_api_secret'
ERPNEXT_URL = 'https://erp.mysite.in'


# operational configs
PULL_FREQUENCY = 30 # in minutes
LOGS_DIRECTORY = 'logs' # logs of this script is stored in this directory
IMPORT_START_DATE = '20230520' # format: '20190501'

# Biometric device configs (all keys mandatory)
    #- device_id - must be unique, strictly alphanumerical chars only. no space allowed.
    #- ip - device IP Address
    #- punch_direction - 'IN'/'OUT'/'AUTO'/None
    #- clear_from_device_on_fetch: if set to true then attendance is deleted after fetch is successful.
                                    #(Caution: this feature can lead to data loss if used carelessly.)
devices = [
    {'device_id':'3','ip':'<DEVICE_IP>', 'punch_direction': None, 'clear_from_device_on_fetch': False},
    {'device_id':'4','ip':'<DEVICE_IP>', 'punch_direction': None, 'clear_from_device_on_fetch': False}
]

# Configs updating sync timestamp in the Shift Type DocType
# shift_type_device_mapping = [
#     {'shift_type_name': ['Shift1'], 'related_device_id': ['test_1','test_2']}
# ]
