# Part One - Calling an API

import requests

api_key = 'h523hDtETbkJ3nSJL323hjYLXbCyDaRZ'
url = 'https://api.recruitment.shq.nz'
client_id = 100

# Function to retrieve a list of domains based on the client id 
def domain_list(client_id):
    response = requests.get(f'{url}/domains/{client_id}', params={'api_key': api_key})
    return response.json()

# Function to retrieve DNS records based on the zone id
def dns_records(zone_id):
    response = requests.get(f'{url}/zones/{zone_id}', params={'api_key': api_key})
    return response.json()


domains = domain_list(client_id)

# Function to print the domains and DNS records
def retrieve(domains):
    print(f"CLIENT {client_id}:")
    for domain in domains:
        print(f"\nDomain: {domain['name']}")
        for zone in domain['zones']:
            print(f"  Zone Name: {zone['name']}")
            # Print DNS records
            zone_id = zone['uri'].split('/')[-1]
            records = dns_records(zone_id)
            print("  DNS Records:")
            for record in records['records']:
                for key, value in record.items():
                    print(f"    {key}: {value}")
                print()

retrieve(domains)
