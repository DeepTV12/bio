import requests
import time

def send_claim_request(token):
    url = "https://api.bio-chain.cc/api/user/receive_airdrop_mining"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "content-length": "0",
        "cookie": "cf_clearance=lI6Q29QWKwDJUKawaE4Ff8vV8zP0Z6FkRLszGREO.PU-1737203968-1.2.1.1-fjKFjUgFEGtApWSmvLikwI0EKWZdVOtYuiRGOlaWGTjMUxzn_vrINV19s3Zb3yKUfYBfr3AtWx1Ug9WhFqvS2gld.oZpHPjU2DHA2rw35xbzymrkZKjHoNDiBpL0ZbZjndJ7fh74WGzUaZQOdgN_Jv1LK7EN15kq4rFBS5uw5.S07QBdhRPiUuYBfO61YweEMUj.9rMddUfPqsgI3D2pcqkg4O2iVt_CXiafOJdB_HOLkDh.gqNrA6TvKJF41M1MAlhB1Je.9I7sIrJjgxEE6w36MGhkkN3VUPaEj0M9dU8",
        "origin": "https://bio-chain.cc",
        "priority": "u=1, i",
        "referer": "https://bio-chain.cc/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "st-ctime": "1737379316314",
        "st-lang": "en",
        "st-ttgn": "30f3c40a88d0ea21d6d489c89804dc6e",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(f"Success: {response.json()}")
        else:
            print(f"Failed for token {token}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending request for token {token}: {e}")

def main():
    try:
        with open("tokens.txt", "r") as file:
            tokens = file.read().splitlines()

        for token in tokens:
            send_claim_request(token)
            time.sleep(1)  # Pause to avoid triggering rate limits

    except FileNotFoundError:
        print("tokens.txt file not found. Please create the file and add your tokens.")

if __name__ == "__main__":
    main()
