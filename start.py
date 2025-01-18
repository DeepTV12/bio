import requests

def start_airdrop_mining(token):
    """Send the start airdrop mining request for a given token."""
    url = "https://api.bio-chain.cc/api/user/start_airdrop_mining"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "content-length": "0",
        "cookie": "cf_clearance=zjQTCFzNzCtypZljSPiXaGSNZb.lMcwLw320HMepS8g-1737203120-1.2.1.1-pzu.s_Im7tNcwbO0KmD3fKZnpOus2taH8nNk08Y3vhU9Fe3tFRR.V1QB0IWY4PvyWpKMIv.JOQ9KGei4tfFxpDqTmYsKPD4FrTI4tJSfowrCs4Tm3RPBxQ5l1xeaRj3aDKICUWJ8XDuQLRCb7pro8q1E3p_EgIL3faW_SuzCU6xBDPMIsfwkNVNQinCraQJS07JlCbGdihqcPrzpfuxgR8SQ0rKZicSa.aP2B8aUWHDJ6Yhrp5qVsDxucoxR8Hpd4Xc24cCZECSSGw4eCqBJ5UVJZ_NmP0YZdebJkzwt7_c",
        "origin": "https://bio-chain.cc",
        "priority": "u=1, i",
        "referer": "https://bio-chain.cc/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "st-ctime": "1737203130959",
        "st-lang": "en",
        "st-ttgn": "9f423205aca4a3f08307a98c7bde8d09",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.post(url, headers=headers)
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending request for token: {token}")
        print(e)
        return None

def main():
    tokens_file = "tokens.txt"
    
    try:
        with open(tokens_file, "r") as file:
            tokens = file.read().splitlines()  # Read all tokens line by line
    except FileNotFoundError:
        print(f"File {tokens_file} not found.")
        return

    for token in tokens:
        print(f"Starting airdrop mining for token: {token}")
        result = start_airdrop_mining(token)
        
        if result:
            print(f"Response: {result}")
        else:
            print(f"Failed to process token: {token}")
        print(f"Finished for all tokens")

if __name__ == "__main__":
    main()
