import requests
import random
import string

def generate_random_email():
    """Generate a random email address."""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@gmail.com"

def register_account(email, password, ref_code):
    """Send a POST request to register a new account."""
    url = "https://api.bio-chain.cc/api/user/register?lang=en"
    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "origin": "https://bio-chain.cc",
        "referer": "https://bio-chain.cc/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    payload = {
        "account": email,
        "pwd": password,
        "user_type": 1,
        "code": ref_code,
        "safety_pwd": password,
        "ws": "",
        "te": "",
        "email_code": "",
        "captcha": ""
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def main():

    hpassword = "08eeb622cee754f996ff22b9e92c5576"
    password = "@DeepTV12"
    accounts_file = "accounts.txt"
    tokens_file = "tokens.txt"
    
    # Get user input
    ref_code = input("Enter the referral code: ")
    n = int(input("How many accounts do you want to create? "))
    
    # Open files in append mode
    with open(accounts_file, "a") as acc_file, open(tokens_file, "a") as tok_file:
        for _ in range(n):
            email = generate_random_email()
            response = register_account(email, hpassword, ref_code)
            
            if response.get("status") == 200:
                token = response["data"]["token"]
                # Append to accounts file
                acc_file.write(f"{email}\n{password}\n{token}\n{'-'*29}\n")
                # Append to tokens file
                tok_file.write(f"{token}\n")
                print(f"Account created: {email}")
            else:
                print(f"Failed to create account for {email}: {response.get('msg', 'Unknown error')}")

if __name__ == "__main__":
    main()
