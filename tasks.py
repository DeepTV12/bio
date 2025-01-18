import requests
import json

def send_task_request(token, task_id):
    """Send the task request for a given token and task ID."""
    url = "https://api.bio-chain.cc/api/user/task_center_receive"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
        "cookie": "cf_clearance=3QcOsV2n_bgBPQxgfhJt4MRTV4ij4phVQpa031IF0qY-1737204574-1.2.1.1-erWqnojTzvKgHN2IVDDHwEvl2LeqbxOMVND8n1tKMSkPtYAdBCcveqRPcdbtmntVEocR63WfztCVbWb.eqw2igmGErMiNPAkDwBTuL7wg79w3oc2qKH9iOXVX0f4t6opdE7bGHYqOQon4SAxBxwJfBwgVGCpPf6N7E_4fteuOIqvxwueWBSsfanp6ge5t6lfiAnBfE0fKera8Ymyu7koy4Fw1BfQLcSkwAepmivzn.JGwBcs9v4iytC1ZqTPob9_pe.4ZgC_xIXkv_wGiXnhfL.8OG7nT8plbomwKlGuD50",
        "origin": "https://bio-chain.cc",
        "priority": "u=1, i",
        "referer": "https://bio-chain.cc/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "st-ctime": "1737204617756",
        "st-lang": "en",
        "st-ttgn": "256988b18568f4689041fb75c662ae0c",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    payload = {"task_id": task_id}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending request for token: {token}, task_id: {task_id}")
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

    task_ids = [9, 7]  # List of task IDs to process

    for token in tokens:
        for task_id in task_ids:
            print(f"Sending task request for token: {token}, task_id: {task_id}")
            result = send_task_request(token, task_id)

            if result:
                print(f"Response for token: {token}, task_id: {task_id}: {result}")
            else:
                print(f"Failed to process token: {token}, task_id: {task_id}")

if __name__ == "__main__":
    main()
