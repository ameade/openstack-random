import os

username = os.environ['OS_USERNAME']
apikey = os.environ['NOVA_API_KEY']
tenant = os.environ['NOVA_PROJECT_ID']
url = os.environ['NOVA_URL']
region = os.environ['NOVA_REGION_NAME']
servicename = os.environ['NOVA_SERVICE_NAME']

users = {
        'komawar': {'key': apikey, 'tenant': tenant},
        'westmaas': {'key': apikey, 'tenant': tenant},
        'blamar': {'key': apikey, 'tenant': tenant},
}

# staging auth conf
auth_url = url
auth_data = {
    'region_name': region,
    'service_name': servicename,
}
