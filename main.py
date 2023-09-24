import requests

def get_public_ip(ipv6=False):
    if ipv6:
        api_url = 'https://api64.ipify.org?format=json'
    else:
        api_url = 'https://api.ipify.org?format=json'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors

        data = response.json()
        return data['ip']
    except requests.exceptions.RequestException as e:
        return str(e)  # Handle request exceptions here

# Example usage
ipv4_address = get_public_ip()
ipv6_address = get_public_ip(ipv6=True)

print(f'IPv4 Address: {ipv4_address}')
print(f'IPv6 Address: {ipv6_address}')
